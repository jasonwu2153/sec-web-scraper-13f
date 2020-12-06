from mysql import connector

# Depending on where your sql server is hosted, 
# you may have to change the host, user, and 
# password values.
db = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="stock_scrape"
)