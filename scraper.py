import csv
import re

import lxml
import requests
from bs4 import BeautifulSoup

sec_url = 'https://www.sec.gov'

def get_request(url):
    'Returns result of a http request to url.'
    return requests.get(url)

def create_url(cik):
    'Returns url of SEC 13F filings given a CIK.'
    return 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&owner=exclude&count=40'.format(cik)

def get_user_input():
    'Prompts user to enter a CIK number.'
    cik = input('Enter 10-digit CIK number: ')
    return cik

# ask user for CIK number
requested_cik = get_user_input()

# find mutual fund by CIK number on EDGAR
response = get_request(create_url(requested_cik))
soup = BeautifulSoup(response.text, 'html.parser')

# get name of mutual fund 
company_name_text = soup.find('span', {'class': 'companyName'}).getText()
company_name = re.sub(' CIK#.*$', '', company_name_text)

# find all document tags; a document tag 
# links to another route containing the 
# relevant filing docs
document_tags = soup.findAll('a', id="documentsbutton")

# for each document tag, try to find the latest primary_doc.xml file
# note that primary_doc.xml files only appear in NPORT-P entries; these 
# are easy to parse so I chose to search for these specifically; if a 
# mututal fund does not have an NPORT-P filing, then nothing is scraped 
for document_tag in document_tags:
    response = get_request(sec_url + document_tag['href'])
    soup = BeautifulSoup(response.text, "html.parser")

    #
    file_tags = soup.findAll(
        'a',
        text='primary_doc.xml',
        attrs={'href': re.compile('.*primary_doc.xml$')}
    )

    # if there are no file tags move on to the next document url
    if len(file_tags) == 0:
        continue

    # ow we parse the primary_doc
    xml_url = file_tags[0].get('href')
    response_xml = get_request(sec_url + xml_url)
    soup_xml = BeautifulSoup(response_xml.content, "lxml")

    # find all invstOrSec tags
    invstOrSecs = soup_xml.body.findAll(re.compile('invstorsec'))
    for invstOrSec in invstOrSecs:
        print(invstOrSec.text)

    break


'''
# Find latest 13F report for mutual fund
response_two = get_request(sec_url + tags[1]['href'])
soup_two = BeautifulSoup(response_two.text, "html.parser")
tags_two = soup_two.findAll('a', attrs={'href': re.compile('xml')})
xml_url = tags_two[0].get('href')

response_xml = get_request(sec_url + xml_url)
soup_xml = BeautifulSoup(response_xml.content, "lxml")

# Find all issuers
issuers = soup_xml.body.findAll(re.compile('nameofissuer'))
for issuer in issuers:
    print(issuer.text)

# Write issuer names to TSV file
with open('{}.tsv'.format(requested_cik), 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for issuer in issuers:
        tsv_writer.writerow([issuer.text])
'''
