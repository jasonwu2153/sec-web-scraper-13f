def insert_sec_company(cik, name):
    'Returns sql statement for inserting one new entry into sec_companies.'
    return f'INSERT INTO sec_companies (cik, name, created_at) VALUES ({cik}, {name}, now());'
