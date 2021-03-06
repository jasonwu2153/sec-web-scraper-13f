# Yale University CPSC 437 Database SEC Python Web Scraper
This repository contains a Python Web scraper for parsing NPORT-P filings (fund holdings) from SEC's website, [EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch.html). We (Jason Wu, Michael Lewkowicz, Kevin Zhang - Yale undergrads) forked this repository from [CodeWritingCow](https://github.com/CodeWritingCow/sec-web-scraper-13f). 

In this fork, we modified the original code to work with the new Edgar website (as of Dec 5th, 2020). These modifications were very signficant. If you look at our web scraper next to the original repo, the code is almost completely different, though we re-use some of the original helper functions written by CodeWritingCow stored in `helper.py`. In addition, we have made the following modifications:

- Exclusively target and scrape NPORT-P filings
- Collect issuers, total value at the time of filing, number of shares, and other relevant data
- Directly insert this data into a mySQL database instead of a tsv file

In addition, note that the documentation is a mix of the original documentation by Gary Pang (CodeWritingCow) and new documentation we've written.

## Requirements

#### Getting Started
- Make sure you have `pipenv` set up on your machine.
- Edit the contents of `db.py` to match the database you are trying to connect to.
- Run `pipenv install`.
- Run `python scraper.py` within a `pipenv shell` (or `pipenv run python scraper.py`).
- When prompted, enter the 10-digit CIK number of a mutual fund.
- Happy investing! ❤️ 💵 💰

#### Key Dependencies

- [Requests](https://2.python-requests.org/en/master/), Python library for making HTTP requests
- [lxml](https://lxml.de/), Python library for processing XML and HTML
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/), Python library for scraping information from Web pages
- [re](https://docs.python.org/3/library/re.html), Python module for using regular expressions
- [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/), Python module for connecting to a MySQL database.

## Contributor
- [Jason Wu (Yale University '22)](https://github.com/jasonwu2153)
- [Kevin Zhang (Yale University '23)](https://github.com/kevinz917)
- [Michael Lewkowicz (Yale University '23)](https://github.com/MLewkowicz)
- [Gary Pang (CodeWritingCow)](https://github.com/CodeWritingCow)

## References
- [SEC: Frequently Asked Questions About Form 13F](https://www.sec.gov/divisions/investment/13ffaq.htm)
