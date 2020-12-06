# Yale University CPSC 437 Database SEC Python Web Scraper
This repository contains a Python Web scraper for parsing 13F filings (mutual fund holdings) from SEC's website, [EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch.html). We (Jason Wu, Michael Lewkowicz, Kevin Zhang - Yale undergrads) forked this repository from [CodeWritingCow](https://github.com/CodeWritingCow/sec-web-scraper-13f). While his repository worked back when it was posted (Jul 18th, 2019), it no longer works due to recent changes to the Edgar website.

In this fork, we modified the original code to work with the new Edgar website (as of Dec 5th, 2020). In addition, we have made the following modifications:

- Exclusively target and scrape NPORT-P filings
- Collect issuers, total value at the time of filing, number of shares, and other relevant data
- Directly insert this data into a mySQL database instead of a tsv file

In addition, note that the documentation is a mix of the original documentation by Gary Pang (CodeWritingCow) and new documentation we've written.

## Requirements

#### Getting Started
- Make sure you have `pipenv` set up on your machine.
- Run `pipenv install`.
- Run `python scraper.py` within a `pipenv shell` (or `pipenv run python scraper.py`).
- When prompted, enter the 10-digit CIK number of a mutual fund.
- Happy investing! 
❤️ 💵 💰

#### Key Dependencies

- [Requests](https://2.python-requests.org/en/master/), Python library for making HTTP requests
- [lxml](https://lxml.de/), Python library for processing XML and HTML
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/), Python library for scraping information from Web pages
- [re](https://docs.python.org/3/library/re.html), Python module for using regular expressions

## Contributor
- [Jason Wu (Yale University '22)](https://github.com/jasonwu2153)
- Kevin Zhang
- Michael Lewkowicz
- [Gary Pang (CodeWritingCow)](https://github.com/CodeWritingCow)

## References
- [SEC: Frequently Asked Questions About Form 13F](https://www.sec.gov/divisions/investment/13ffaq.htm)
