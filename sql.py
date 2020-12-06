def insert_sec_company(cik, name):
    'Returns sql statement for inserting one new entry into sec_companies table.'
    return f'INSERT INTO sec_companies (cik, name, created_at) VALUES ({cik}, {name}, now());'

def insert_stocks(stocks):
    '''
    Takes in an array of stock dictionaries formatted like so:

    {
        'isin': 'value',
        'name': 'value',
        'title': 'value',
        'lei': 'value',
        'cusip': 'value'
    }

    Returns sql statement for inserting all of the stock entries into stocks table.
    '''
    pass 

def insert_holdings(holdings):
    '''
    Takes in array of holding dictionaries formatted like so:

    {
        'held_by': 'value',
        'isin': 'value',
        'units': 'value',
        'balance': 'value',
        'val_usd': 'value'
    }

    Returns sql statement for inserting all of the holding entries into holdings table.
    '''
    pass