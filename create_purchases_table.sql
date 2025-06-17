USE Book_Insights_Project;

CREATE TABLE Purchases (
    Purchase_ID INT PRIMARY KEY,
    Customer_ID INT,
    Book_ID INT, 
    Purchase_Date DATE,
    Quantity INT, 
    Total_Price REAL,
    FOREIGN KEY(Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY(Book_ID) REFERENCES Books(Book_ID)
);

INSERT INTO Purchases (Purchase_ID, Customer_ID, Book_ID, Purchase_Date, Quantity, Total_Price) VALUES
(1, 2, 0, '2025-02-26', 4, 80.56),
(2, 1, 1, '2025-02-16', 2, 30.00),
(3, 3, 2, '2025-02-12', 3, 36.00);

select * from purchases;


