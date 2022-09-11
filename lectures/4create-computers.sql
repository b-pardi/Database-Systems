-- SQLite
DROP TABLE Product;
DROP TABLE PC;
DROP TABLE Laptop;
DROP TABLE Printer;

CREATE TABLE Product (
    maker CHAR(32),
    model INTEGER PRIMARY KEY,
    type VARCHAR(20) NOT NULL
);

CREATE TABLE PC (
    model INTEGER PRIMARY KEY,
    speed FLOAT,
    ram INTEGER,
    hd INTEGER,
    price DECIMAL(7,2) NOT NULL
);

CREATE TABLE Laptop (
    model INTEGER PRIMARY KEY,
    speed FLOAT,
    ram INTEGER,
    hd INTEGER,
    screen DECIMAL(4,1),
    price DECIMAL(7,2) NOT NULL
);

CREATE TABLE Printer (
    model INTEGER PRIMARY KEY,
    color BOOL,
    type VARCHAR(30),
    price decimal(7,2) NOT NULL
);

