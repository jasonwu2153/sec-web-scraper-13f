def insert_sec_company_sql(cik, name):
    'Returns sql statement for inserting one new entry into sec_companies table.'
    return f'INSERT INTO sec_companies (cik, name, created_at) VALUES ({cik}, {name}, now());'

def insert_stocks_sql(stocks):
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
    header = 'INSERT INTO stocks (isin, name, title, lei, cusip, created_at) VALUES'
    stock_values = map(lambda x: f'('{x['isin']}', '{x['name']}', '{x['title']}', '{x['lei']}', '{x['cusip']}', now())', stocks)
    value_string = ', '.join(stock_values)
    return header + ' ' +  value_string + ';'

def insert_holdings_sql(holdings):
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