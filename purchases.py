import pandas as pd
import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta, date

fake = Faker()
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# the purchases table will be connecting with the books and customers table, so I need grab data from both tables
customer_ids = pd.read_sql_query("SELECT Customer_ID FROM Customers", conn)['Customer_ID'].tolist()
book_df = pd.read_sql_query("SELECT Book_ID, Price, Published_Date FROM BOOKS", conn)

# create purchases
num_purchases = 100
purchases = []

# convert published year to a date time object
year_start = date(2025, 1, 1)
today = date.today()

for purchase_id in range (1, num_purchases + 1):
    customer_id = random.choice(customer_ids)

    # random books that will be purchased
    book_row = book_df.sample(1).iloc[0]
    book_id = book_row['Book_ID']
    book_price = book_row['Price']
    published_year = int(book_row['Published_Date'])
    start_date = datetime(published_year, 1, 1)

    # published date cannot be passed its original date
    if start_date.date() > today:
        start_date = today

    # create a fake purchase date between publication date and today's date
    purchase_date = fake.date_between(start_date=max(start_date.date(), year_start), end_date=today)

    # generate random quantity and calculations of purchases - quantity caps at 5
    quantity = random.randint(1, 5)
    total_price = round(quantity * book_price, 2)

    # store the purchase data
    purchases.append((purchase_id, customer_id, book_id, purchase_date, quantity, total_price))

df_purchases = pd.DataFrame(
    purchases,
    columns=['Purchase_ID', 'Customer_ID', 'Book_ID', 'Purchase_Date', 'Quantity', 'Total_Price']
    )

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Purchases (
        Purchase_ID INTEGER PRIMARY KEY,
        Customer_ID INTEGER,
        Book_ID INTEGER,
        Purchase_Date DATE,
        Quantity INTEGER,
        Total_Price REAL,
        FOREIGN KEY(Customer_ID) REFERENCES Customers(Customer_ID),
        FOREIGN KEY(Book_ID) REFERENCES Books(Book_ID)
    )
''')
# Insert the purchase data into the database books.db
df_purchases.to_sql('Purchases', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("Purchases table has been created successfully.")
