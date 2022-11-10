import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
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


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    try:
        sql = """CREATE TABLE warehouse (
                    w_warehousekey decimal(9,0) not null,
                    w_name char(100) not null,
                    w_capacity decimal(6,0) not null,
                    w_suppkey decimal(9,0) not null,
                    w_nationkey decimal(2,0) not null
                    )"""
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as exc:
        _conn.rollback()
        print(exc)

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = "DROP TABLE warehouse"
        _conn.execute(sql)
        _conn.commit()
        print("success")
    except Error as exc:
        _conn.rollback()
        print(exc)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    try:
        # query to grab nations for each supp, with most lineitems ordered by custs in that nation
        sql_loc = """select s_name, n_name, count(l_quantity) as ct
            from supplier, nation, customer, lineitem, orders
            where s_suppkey = l_suppkey
            and l_orderkey = o_orderkey
            and o_custkey = c_custkey
            and c_nationkey = n_nationkey

            group by s_name, n_name
            order by s_name, ct desc
        """
        cur = _conn.cursor()
        warehouse_names = []
        cur.execute(sql_loc)
        # grab all rows returned from query
        warehouse_locs = cur.fetchall()
        quantity = 0
        # only need first 2 entries for each supplier
        # ordered in descending order grouped by supplier,
        # so count decreases for each supp and then increases when next supp occurs
        
        for i in range(len(warehouse_locs)):
            if quantity < warehouse_locs[i][2]:
                warehouse_names.append(warehouse_locs[i][0] + '___' + warehouse_locs[i][1])
                warehouse_names.append(warehouse_locs[i+1][0] + '___' + warehouse_locs[i+1][1])
            quantity = warehouse_locs[i][2]
   
        print(warehouse_names)

        sql_cap = """select s_name, n_name, ct, max(cap)
                from(select s_name, n_name, count(l_quantity) as ct, sum(p_size) * 2 as cap
                    from supplier, nation, customer, lineitem, orders, part
                    where s_suppkey = l_suppkey
                    and l_orderkey = o_orderkey
                    and o_custkey = c_custkey
                    and c_nationkey = n_nationkey
                    and l_partkey = p_partkey

                    group by s_name, n_name
                    order by s_name, ct desc)
                group by s_name
        """
        cur = _conn.cursor()
        cur.execute(sql_cap)
        # grab all rows returned from query
        warehouse_caps = cur.fetchall()
        print(warehouse_caps)

        # wId, wName, wCap, sId, nId
        warehouses = []
        for i in range(len(warehouse_names)):
            sID = int(warehouse_locs[i][0][-4:])
            entry = (i, warehouse_names[i], warehouse_caps[i][3], sID)
            warehouses.append(entry)



        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
            
        populateTable(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
