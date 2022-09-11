-- SQLite
-- https://sqlite.org/lang_createtable.html


CREATE TABLE Cities_Loc (
    name CHAR(50) PRIMARY KEY,
    latitude DECIMAL(8,6),
    longitude DECIMAL(9,6)
);

CREATE TABLE Cities_Population (
    county CHAR(50) NOT NULL,
    city CHAR(50) PRIMARY KEY,
    incorporated INTEGER,
    pop_1980 INTEGER,
    pop_1990 INTEGER,
    pop_2000 INTEGER,
    pop_2010 INTEGER
);


ALTER TABLE Cities_Population
    ADD COLUMN pop_2020 INTEGER;
