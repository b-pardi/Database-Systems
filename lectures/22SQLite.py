import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")

    try:
        sql = """CREATE TABLE Product (
                    maker CHAR(32),
                    model INTEGER PRIMARY KEY,
                    type VARCHAR(20) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE PC (
                    model INTEGER PRIMARY KEY,
                    speed FLOAT,
                    ram INTEGER,
                    hd INTEGER,
                    price DECIMAL(7,2) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Laptop (
                model INTEGER PRIMARY KEY,
                speed FLOAT,
                ram INTEGER,
                hd INTEGER,
                screen DECIMAL(4,1),
                price DECIMAL(7,2) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Printer (
                model INTEGER PRIMARY KEY,
                color BOOL,
                type VARCHAR(30),
                price decimal(7,2) NOT NULL)"""
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = "DROP TABLE Product"
        _conn.execute(sql)

        sql = "DROP TABLE PC"
        _conn.execute(sql)

        sql = "DROP TABLE Laptop"
        _conn.execute(sql)

        sql = "DROP TABLE Printer"
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Product(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate PRODUCT")

    try:
        products = [
            ('A', 1001, 'pc'),
            ('A', 1002, 'pc'),
            ('A', 1003, 'pc'),
            ('A', 2004, 'laptop'),
            ('A', 2005, 'laptop'),
            ('A', 2006, 'laptop'),

            ('B', 1004, 'pc'),
            ('B', 1005, 'pc'),
            ('B', 1006, 'pc'),
            ('B', 2007, 'laptop'),

            ('C', 1007, 'pc'),

            ('D', 1008, 'pc'),
            ('D', 1009, 'pc'),
            ('D', 1010, 'pc'),
            ('D', 3004, 'printer'),
            ('D', 3005, 'printer'),

            ('E', 1011, 'pc'),
            ('E', 1012, 'pc'),
            ('E', 1013, 'pc'),
            ('E', 2001, 'laptop'),
            ('E', 2002, 'laptop'),
            ('E', 2003, 'laptop'),
            ('E', 3001, 'printer'),
            ('E', 3002, 'printer'),
            ('E', 3003, 'printer'),

            ('F', 2008, 'laptop'),
            ('F', 2009, 'laptop'),

            ('G', 2010, 'laptop'),

            ('H', 3006, 'printer'),
            ('H', 3007, 'printer')
        ]

        sql = "INSERT INTO Product VALUES(?, ?, ?)"
        _conn.executemany(sql, products)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insert_PC(_conn, _model, _speed, _ram, _hd, _price):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert PC")

    try:
        sql = """INSERT INTO PC(model, speed, ram, hd, price)
            VALUES(?, ?, ?, ?, ?)"""
        args = [_model, _speed, _ram, _hd, _price]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_PC(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate PC")

    insert_PC(_conn, 1001, 2.66, 1024, 250, 2114)
    insert_PC(_conn, 1002, 2.10, 512, 250, 995)
    insert_PC(_conn, 1003, 1.42, 512, 80, 478)
    insert_PC(_conn, 1004, 2.80, 1024, 250, 649)
    insert_PC(_conn, 1005, 3.20, 512, 250, 630)
    insert_PC(_conn, 1006, 3.20, 1024, 320, 1049)
    insert_PC(_conn, 1007, 2.20, 1024, 200, 510)
    insert_PC(_conn, 1008, 2.20, 2048, 250, 770)
    insert_PC(_conn, 1009, 2.00, 1024, 250, 650)
    insert_PC(_conn, 1010, 2.80, 2048, 300, 770)
    insert_PC(_conn, 1011, 1.86, 2048, 160, 959)
    insert_PC(_conn, 1012, 2.80, 1024, 160, 649)
    insert_PC(_conn, 1013, 3.06, 512, 80, 529)

    print("success")
    print("++++++++++++++++++++++++++++++++++")


def insert_Laptop(_conn, _model, _speed, _ram, _hd, _screen, _price):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Laptop")

    try:
        sql = "INSERT INTO Laptop VALUES(?, ?, ?, ?, ?, ?)"
        args = [_model, _speed, _ram, _hd, _screen, _price]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Laptop(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Laptop")

    insert_Laptop(_conn, 2001, 2.00, 2048, 240, 20.1, 3673)
    insert_Laptop(_conn, 2002, 1.73, 1024, 80, 17.0, 949)
    insert_Laptop(_conn, 2003, 1.80, 512, 60, 15.4, 549)
    insert_Laptop(_conn, 2004, 2.00, 512, 60, 13.3, 1150)
    insert_Laptop(_conn, 2005, 2.16, 1024, 120, 17.0, 2500)
    insert_Laptop(_conn, 2006, 2.00, 2048, 80, 15.4, 1700)
    insert_Laptop(_conn, 2007, 1.83, 1024, 120, 13.3, 1429)
    insert_Laptop(_conn, 2008, 1.60, 1024, 100, 15.4, 900)
    insert_Laptop(_conn, 2009, 1.60, 512, 80, 14.1, 680)
    insert_Laptop(_conn, 2010, 2.00, 2048, 160, 15.4, 2300)

    print("success")
    print("++++++++++++++++++++++++++++++++++")


def insert_Printer(_conn, _model, _color, _type, _price):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Printer")

    try:
        sql = """INSERT INTO Printer(model, color, type, price)
                VALUES(?, ?, ?, ?)"""
        args = [_model, _color, _type, _price]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Printer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Printer")

    insert_Printer(_conn, 3001, True, "ink-jet", 99)
    insert_Printer(_conn, 3002, False, "laser", 239)
    insert_Printer(_conn, 3003, True, "laser", 899)
    insert_Printer(_conn, 3004, True, "ink-jet", 120)
    insert_Printer(_conn, 3005, False, "laser", 120)
    insert_Printer(_conn, 3006, True, "ink-jet", 100)
    insert_Printer(_conn, 3007, True, "laser", 200)

    print("success")
    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    populateTable_Product(_conn)
    populateTable_PC(_conn)
    populateTable_Laptop(_conn)
    populateTable_Printer(_conn)


def pcsByMaker(_conn, _maker):
    print("++++++++++++++++++++++++++++++++++")
    print("PCs by maker: ", _maker)

    try:
        sql = """select P.model as model, PC.price as price
                from Product P, PC
                where P.model = PC.model AND
                maker = ?"""
        args = [_maker]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def productByMaker(_conn, _pType, _maker):
    print("++++++++++++++++++++++++++++++++++")
    print(_pType, " by maker: ", _maker)

    try:
        sql = """select P.model as model,
            {}.price as price
            from Product P, {}
            where P.model = {}.model AND
            maker = ?""".format(_pType, _pType, _pType)
        args = [_maker]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10}'.format("model", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def allProductsByMaker(_conn, _maker):
    print("++++++++++++++++++++++++++++++++++")
    print("Products by maker: ", _maker)

    try:
        sql = """select P.model as model, P.type as type, PC.price as price
            from Product P, PC
            where P.model = PC.model AND
            maker = ?
            UNION
            select P.model as model, P.type as type, L.price as price
            from Product P, Laptop L
            where P.model = L.model AND
            maker = ?
            UNION
            select P.model as model, P.type as type, Pr.price as price
            from Product P, Printer Pr
            where P.model = Pr.model AND
            maker = ?"""
        args = [_maker, _maker, _maker]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>20} {:>10}'.format("model", "type", "price")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>10}'.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTables(conn)
        #createTables(conn)
        #populateTables(conn)

        pcsByMaker(conn, "E")
        productByMaker(conn, "Laptop", "E")
        allProductsByMaker(conn, "E")

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
