'''
Note that in the insertion statements below, we use INSERT IGNORE. This is because
checking whether a stock has already been inserted into the database before insertion 
every single time is expensive. Instead, if we get a duplicate key error we ignore it. 
'''
insert_sec_company_sql = 'INSERT INTO sec_companies (cik, name, created_at) VALUES (%s, %s, now());'
insert_legal_entity_sql = 'INSERT IGNORE INTO legal_entities (lei, name, title, created_at) VALUES (%s, %s, %s, now());'
insert_holdings_sql = 'INSERT IGNORE INTO holdings (held_by, lei, isin, cusip, units, balance, val_usd, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, now());'

check_sec_company_present = 'SELECT * FROM sec_companies WHERE cik = %s;'