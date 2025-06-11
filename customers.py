import pandas as pd
import sqlite3
from faker import Faker
import random

# these are the 50 states that will be randomized in the table
fake = Faker()
us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

# 50 customers will be created for this table
num_customers = 50
customers = [] # this is where the rows of customers will be held

# for loop that will loop through the customer_id from 1-50
for customer_id in range(1, num_customers + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        number = random.randint(10, 99)
        email = f"{first_name.lower()}{last_name.lower()}{number}@gmail.com"
        location = random.choice(us_states)
        customers.append((customer_id, first_name, last_name, email, location))

df_customers = pd.DataFrame(customers, columns=['Customer_ID', 'First_Name', 'Last_Name', 'Email', 'Location'])

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        Customer_ID INTEGER PRIMARY KEY,
        First_Name TEXT,
        Last_Name TEXT,
        Email TEXT,
        Location TEXT
    )
''')

df_customers.to_sql('Customers', conn, if_exists='replace',index=False)

conn.commit()
conn.close()

# when this script is run, this message will be presented to let me know that it was a success
print("Customers table has been created successfully.")