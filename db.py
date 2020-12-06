from mysql import connector

# Depending on where your sql server is hosted, 
# you may have to change the host, user, and 
# password values.
cnx = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sec_scrape"
)