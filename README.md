# 📚 Book Insights Project

As an avid reader with a slight book-buying addiction, I wanted to combine my love for reading with my growing skills in data analytics and QA automation. 

This project combines all the books I've read in 2024 and 2025 using Python and SQL, and serves as a foundation to showcase my ability to create, manipulate, and test data through realistic, hands-on projects.

What started as a fun way to organize my reading list turned into a technical playground for learning database design, data validation, and automated testing.

---

## Tech Stack

- 🐍 Python (with Faker)
- SQLite
- pandas

---

## Project Overview

I created three main tables using Python and SQLite:

- **Books**: real book titles with authors, genres, prices, published dates, and formats (Paperback, eBook, or Hardcover)
- **Customers**: fake customers data generated with the `Faker` library 
- **Purchases**: connects readers (customers table) to the books they've "purchased", (purchases table) including realistic purchase dates

This is the first version of the project, with clean and well-structured data.

---

## Files
- `books_import_genre_column_updated.py`: creates the `Books` table **This file has been renamed to books_dataset.py**
- `customers.py`: generates fake customer data
- `purchases.py`: creates the `Purchases` table using joined data

---

📂 SQL-Only Table Scripts

To demonstrate that I can also manually write SQL and create tables without relying on Python or CSVs, I created standalone `.sql` files for each table. These files show my ability to design clean, relational databases using SQL alone:

- `books_table.sql` – Books catalog schema with sample data  
- `customers_table.sql` – Customers table with sample Faker-style data  
- `purchases_table.sql` – Purchases records referencing both books and customers 

These scripts reflect proper data typing, constraints, and table relationships and are meant to highlight my SQL-only skills as part of this evolving project.

---

## 📝 Note on File Versions

- `books_import.py`: this is my original script used to read my Goodreads CSV and create the `Books` table. This version pulled genres from the "Bookshelves" column of my Goodreads csv file, which led to inaccurate genre classifications of the books, and I had to manually update the csv file with the correct genre.
- `books_import_genre_column_updated.py`: this is the updated version with a manually corrected genre column. This script is the one used to create the clean, accurate `Books` table in the final database. **This file has been renamed to books_dataset.py**

Both files are included to show the evolution of the project and my learning process.

---

## 🚀 How to Run

Make sure you have the required libraries installed.  
In your Terminal, run:

```
pip install faker
pip install pandas
pip install sqlite
```
---

## Then run each script in Terminal:

```
python books.py
python customers.py
python purchases.py
```

This will create a database called "books.db" with all the books, customers, and purchase data.

---

## 🧠 Future Additions

- Introduce intentionally “dirty” or inconsistent data (e.g., NULLs, typos, incorrect formats)
- Write SQL queries to validate and clean data (as a QA engineer would in real scenarios)
- Add a qa_issues.sql file simulating bug-hunting and test case creation
- Visualize insights (e.g., most purchased genres or top authors)

---

✨ What I’m Learning

- How to connect Python and SQL to create realistic, testable datasets
- Data modeling and relationships between tables
- How to test and validate data using SQL queries
- Building hands-on portfolio projects as a future QA Automation Engineer

---

Final Thoughts 

This is an evolving project and a reflection of my learning journey. If this project were a book, we’d still be in Chapter One. Come back for the plot twists. 📖✨
