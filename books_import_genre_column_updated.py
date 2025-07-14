import os

import pandas as pd
import numpy as np
import sqlite3

# Read the corrected CSV with updated genre info
# Updated the csv file name to make it shorter and easier to remember since I have made more than one specific change so far
df_books = pd.read_csv("books_dataset.csv")

# Reorder columns if needed. This is optional but it also reassures that this needs to be the order
df_books = df_books[['Book_ID', 'Title', 'Author', 'Genre', 'Price', 'Published_Date', 'Format']]

# Connect to SQLite database
conn = sqlite3.connect('books.db')
df_books.to_sql('Books', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
