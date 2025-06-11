import pandas as pd
import numpy as np
import sqlite3

# I want to add the csv
df = pd.read_csv("books_genre_column_fix.csv")

# Now choose and rename relevant columns
df_books = df[['Title', 'Author', 'Bookshelves', 'Year Published', 'Binding']].copy()
df_books.columns = ['Title', 'Author', 'Genre', 'Published_Date', 'Format']

# I want to add columns book_id, and price to the table
df_books.insert(0, 'Book_ID', range(1, len(df_books) + 1))
df_books['Price'] = np.round(np.random.uniform(5.99, 29.99, size=len(df_books)), 2)

# I realized that the Genre column doesn't have the correct genre
# for each book since it's pulling from the Bookshelves column in the goodreads csv
# so I need to create a file I can open in Excel to manually input the correct genre for each book
# df_books.to_csv("books_genre_column_fix.csv", index=False)

# Now I want to reorder how the columns present themselves in the table
df_books = df_books[['Book_ID', 'Title', 'Author', 'Genre', 'Price', 'Published_Date', 'Format']]

# Connect to SQLite database and table
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Book_ID INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Genre TEXT,
        Price REAL,
        Published_Date INTEGER,
        Format TEXT
    )
''')

# Step 6: Insert data into the Books table
df_books.to_sql('Books', conn, if_exists='replace', index=False)

# Step 7: Finish
conn.commit()
conn.close()
