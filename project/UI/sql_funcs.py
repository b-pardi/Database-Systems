import sqlite3
from sqlite3 import Error

def openConnection(db):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", db)

    conn = None
    try:
        conn = sqlite3.connect(db)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(conn, db):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", db)

    try:
        conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def queryDB(conn, sql, args=[]):
    try:
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("++++++++++++++++++++++++++++++++++\nQuery Process Success\n")
        print(f"arguments: {args}")
        rows = cur.fetchall()
        if len(rows) == 0:
            print("No results matched query")
        else:
            print("Results:")
            for row in rows:
                print(row)

    except Error as err:
        conn.rollback()
        print(err)

