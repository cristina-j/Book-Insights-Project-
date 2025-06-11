import os

import pandas as pd
import numpy as np
import sqlite3

# Read the corrected CSV with updated genre info
df_books = pd.read_csv("books_genre_column_updated.csv")

# Optional: Reorder columns if needed
df_books = df_books[['Book_ID', 'Title', 'Author', 'Genre', 'Price', 'Published_Date', 'Format']]

# Connect to SQLite database
conn = sqlite3.connect('books.db')
df_books.to_sql('Books', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
