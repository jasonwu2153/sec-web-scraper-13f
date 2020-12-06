import re

import lxml
from bs4 import BeautifulSoup
from tqdm import tqdm

from db import cnx
from helpers import create_url, get_request, get_user_input, sec_url
from sql import check_sec_company_present, insert_sec_company_sql, insert_stocks_sql, insert_holdings_sql

def main():
    # ask user for CIK number
    requested_cik = get_user_input()

    # find mutual fund by CIK number on EDGAR
    response = get_request(create_url(requested_cik))
    soup = BeautifulSoup(response.text, 'html.parser')

    # get name of mutual fund 
    company_name_text = soup.find('span', {'class': 'companyName'}).getText()
    company_name = re.sub(' CIK#.*$', '', company_name_text)

    # find all document tags; a document tag links to another 
    # route containing the relevant filing docs
    document_tags = soup.findAll('a', id="documentsbutton")

    # for each document tag, try to find the latest primary_doc.xml file
    # note that primary_doc.xml files only appear in NPORT-P entries; these 
    # are easy to parse so I chose to search for these specifically; if a 
    # mututal fund does not have an NPORT-P filing, then nothing is scraped 
    for document_tag in document_tags:
        response = get_request(sec_url + document_tag['href'])
        soup = BeautifulSoup(response.text, "html.parser")

        # find file tag labeled primary_doc.xml; this is the 
        # standard filename for NPORT-P filings
        file_tag = soup.find(
            'a',
            text='primary_doc.xml',
            attrs={'href': re.compile('.*primary_doc.xml$')}
        )

        # if there is no primary_doc.xml skip this document page
        if file_tag is None:
            continue

        print(f'\nScraping Data from {company_name} (CIK: {requested_cik})...')
        print('--------------------------------------------------------------')
        print('Fetching xml file... ⌛')

        # scrape & parse the xml file
        xml_url = file_tag.get('href')
        response_xml = get_request(sec_url + xml_url)
        soup_xml = BeautifulSoup(response_xml.content, "lxml")

        print('Xml file fetched! 😊')
        print('\nParsing Progress:')

        stock_data = []
        holdings_data = []

        # find all holdings
        invstOrSecs = soup_xml.body.findAll(re.compile('invstorsec'))
        for invstOrSec in tqdm(invstOrSecs, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            stock = {}
            holding = { 'held_by': requested_cik }

            # parse isin (if there is no isin value we skip it)
            isin_text = invstOrSec.find('identifiers').find('isin')
            if not isin_text:
                continue 
            stock['isin'] = isin_text.get('value')
            holding['isin'] = isin_text.get('value')

            # parse name and title
            name_text = invstOrSec.find('name').text
            title_text = invstOrSec.find('title').text
            stock['name'] = name_text if name_text != 'N/A' else None
            stock['title'] = title_text if title_text != 'N/A' else None

            # parse lei and cusip
            lei_text = invstOrSec.find('lei').text
            cusip_text = invstOrSec.find('cusip').text 
            stock['lei'] = lei_text if lei_text != 'N/A' else None 
            stock['cusip'] = cusip_text if cusip_text != 'N/A' else None 

            # parse units, balance, and value in USD if applicable (if the 
            # value is not in USD we skip it)
            units_text = invstOrSec.find('units').text
            balance_text = invstOrSec.find('balance').text
            val_usd_text = invstOrSec.find('valusd').text
            holding['units'] = units_text if units_text != 'N/A' else None 
            holding['balance'] = int(float(balance_text)) if balance_text != 'N/A' else 0
            holding['val_usd'] = int(float(val_usd_text)) if val_usd_text != 'N/A' else 0

            # store data
            stock_data.append(stock)
            holdings_data.append(holding)

        # create db cursor
        cursor = cnx.cursor()

        # check if cik number already in database
        cursor.execute(check_sec_company_present, (requested_cik,))
        results = cursor.fetchall()
        if len(results) > 0:
            print('\nExiting without updating database since this company/mutual fund has already been scraped.')
            cursor.close()
            cxn.close()
            break

        # upsert current company/mutual fund to sec_companies table
        print('\nAdding company/mutual fund to sec_companies table...')
        cursor.execute(insert_sec_company_sql, (requested_cik, company_name))
        print('Updated sec_companies table successfully. 👍')

        # upsert each stock to stock table
        print('\nAdding stocks to stocks table...')
        stock_tuples = list(map(lambda x: (x['isin'], x['name'], x['title'], x['lei'], x['cusip']), stock_data))
        cursor.executemany(insert_stocks_sql, stock_tuples)
        print('Updated stocks table successfully. 👍')

        # add each holding to holdings table
        print('\nAdding holdings to holdings table...')
        holding_tuples = list(map(lambda x: (x['held_by'], x['isin'], x['units'], x['balance'], x['val_usd']), holdings_data))
        cursor.executemany(insert_holdings_sql, holding_tuples)
        print('Updated holdings table successfully. 👍')

        # commit changes to database
        cnx.commit()

        # close connection
        cursor.close()
        cnx.close()

        break

if __name__ == '__main__':
    main()