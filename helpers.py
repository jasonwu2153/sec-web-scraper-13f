import requests

sec_url = 'https://www.sec.gov'

def get_request(url):
    'Returns result of a http request to url.'
    return requests.get(url)

def create_url(cik):
    'Returns url of SEC 13F filings given a CIK.'
    return f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&owner=exclude&count=40'

def get_user_input():
    'Prompts user to enter a CIK number.'
    cik = input('Enter 10-digit CIK number: ')
    return cik