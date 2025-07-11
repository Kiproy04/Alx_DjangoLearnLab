CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE IF NOT EXISTS Books(
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT FOREIGN KEY REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE,
);

CREATE TABLE IF NOT EXISTS Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215),
);

CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT,
);

CREATE TABLE IF NOT EXISTS Orders(
    order_id INT PRIMARY KEY,
    customer_id FOREIGN KEY (customer_id) REFERENCES Customers(customer_id), 
    order_date DATE,
);

CREATE TABLE IF NOT EXISTS Order_Details(
    order_detail INT PRIMARY KEY,
    order_id FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    book_id FOREIGN KEY (book_id) REFERENCES Books(book_id),
    quantity DOUBLE,
);
