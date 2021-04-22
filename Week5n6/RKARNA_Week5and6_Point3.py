import sqlite3
import pandas as pd

query = """
CREATE TABLE customer_data
(Name VARCHAR(20), Address VARCHAR(20),
 City VARCHAR(20), State VARCHAR(20),
 Zip REAL, PhoneNo INTEGER
);"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Raja1', '1 James St', 'Darsi', 'VA', 23224, 1134567890),
        ('Raja2', '2 James St', 'Darsi', 'VA', 23224, 1234567890),
        ('Raja3', '3 James St', 'Darsi', 'VA', 23224, 1334567890),
        ('Raja4', '4 James St', 'Darsi', 'VA', 23224, 1434567890),
        ('Raja5', '5 James St', 'Darsi', 'VA', 23224, 1534567890),
        ('Raja6', '6 James St', 'Darsi', 'VA', 23224, 1634567890),
        ('Raja7', '5 James St', 'Darsi', 'VA', 23224, 1734567890),
        ('Raja8', '8 James St', 'Darsi', 'VA', 23224, 1834567890),
        ('Raja9', '9 James St', 'Darsi', 'VA', 23224, 1934567890),
        ('Raja10', '10 James St', 'Darsi', 'VA', 23224, 1104567890)]
stmt = "INSERT INTO customer_data VALUES(?, ?, ?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from customer_data')
rows = cursor.fetchall()
rows
pd.read_sql('select * from customer_data', con)