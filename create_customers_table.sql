USE Book_Tracker;

CREATE TABLE Customers (
Customer_ID INT PRIMARY KEY,
First_Name TEXT NOT NULL,
Last_Name TEXT NOT NULL,
Email TEXT,
Location TEXT
);


INSERT INTO Customers (Customer_ID, First_Name, Last_Name, Email, Location) VALUES
(1, 'Anya', 'Johnson', 'anyajohnson59@gmail.com', 'NC'),
(2, 'Vivian', 'Young', 'vivianyoung02@gmail.com', 'CA'),
(3, 'Liam', 'Smith', 'liamsmith12@gmail.com', 'GA');

select * from Customers;




