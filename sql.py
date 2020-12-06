'''
Note that in the insertion statements below, we use INSERT IGNORE. This is because
checking whether a stock has already been inserted into the database before insertion 
every single time is expensive. Instead, if we get a duplicate key error we ignore it. 
'''

insert_sec_company_sql = 'INSERT IGNORE INTO sec_companies (cik, name, created_at) VALUES (%s, %s, now());'

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
    header = 'INSERT IGNORE INTO stocks (isin, name, title, lei, cusip, created_at) VALUES'
    stock_values = map(lambda x: f'(\'{x["isin"]}\', \'{x["name"]}\', \'{x["title"]}\', \'{x["lei"]}\', \'{x["cusip"]}\', now())', stocks)
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
    header = 'INSERT IGNORE INTO holdings (held_by, isin, units, balance, val_usd, created_at) VALUES'
    holding_values = map(lambda x: f'(\'{x["held_by"]}\', \'{x["isin"]}\', \'{x["units"]}\', {x["balance"]}, {x["val_usd"]})', holdings)
    value_string = ', '.join(holding_values)
    return header + ' ' + value_string + ';'