CREATE DATABASE Book_Insights_Project;
USE Book_Insights_Project;

CREATE TABLE Books(
Book_ID INT Primary KEY,
Title VARCHAR(225) NOT NULL,
Author VARCHAR(225) NOT NULL,
Genre VARCHAR(100),
Price DECIMAL(6,2), 
Published_Date YEAR,
Format ENUM('Paperback', 'Hardcover', 'eBook')
);

INSERT INTO Books (Book_ID, Title, Author, Genre, Price, Published_Date, Format) VALUES 
(0, 'King of Envy', 'Ana Huang', 'Romance', 20.00, '2025', 'Paperback'),
(1, 'First Time Caller', 'B.K. Riorson', 'Romance', 15.00, '2025', 'Paperback'),
(2, 'Done and Dusted', 'Lyla Sage', 'Romance', 18.00, '2023', 'Paperback');

Select * from books;