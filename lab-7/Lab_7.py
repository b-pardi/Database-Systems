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
        # query finds where nations have warehouses for each supp
        sql_nat_name = """select s_name, n_name, count(l_quantity) as ct, sum(p_size) * 2 as cap, n_nationkey as nk
        from supplier, nation, customer, lineitem, orders, part
        where s_suppkey = l_suppkey
        and l_orderkey = o_orderkey
        and o_custkey = c_custkey
        and c_nationkey = n_nationkey
        and l_partkey = p_partkey

        group by s_name, n_name
        order by s_name, ct desc, n_name
        """
        cur = _conn.cursor()
        cur.execute(sql_nat_name)
        warehouse_nats = cur.fetchall()
        warehouse_names = []
        ct = 0
        # sql query above returns descending list of count for each nation for each supp
        # compare ct to ct of table, when it increases it means next supplier
        # grab first 2 of each supp
        for i in range(len(warehouse_nats)-1):
            if ct < warehouse_nats[i][2]:
                n1 = warehouse_nats[i][0] + '___' + warehouse_nats[i][1]
                n2 = warehouse_nats[i+1][0] + '___' + warehouse_nats[i+1][1]
                warehouse_names.append((n1, warehouse_nats[i][4]))
                warehouse_names.append((n2, warehouse_nats[i+1][4]))
            ct = warehouse_nats[i][2]

        # modify to query to find max cap for each supps nation
        sql_caps = """select s_name, n_name, ct, max(cap)
            from (select s_name, n_name, count(l_quantity) as ct, sum(p_size) * 2 as cap
                from supplier, nation, customer, lineitem, orders, part
                where s_suppkey = l_suppkey
                and l_orderkey = o_orderkey
                and o_custkey = c_custkey
                and c_nationkey = n_nationkey
                and l_partkey = p_partkey

                group by s_name, n_name
                order by s_name, ct desc)
            group by s_name
            order by s_name, ct desc"""
        cur.execute(sql_caps)
        warehouse_caps = cur.fetchall()

        # put together tuples for warehouses
        # wId, wName, wCap, sId, nId
        warehouses = []
        for i in range(len(warehouse_names)):
            wId = i+1
            wName = warehouse_names[i][0]
            wCap = warehouse_caps[int(i/2)][3]
            sId = int(i/2)+1
            nId = warehouse_names[i][1]
            warehouse = (wId, wName, wCap, sId, nId)
            warehouses.append(warehouse)

        #print(warehouses)

        # insert warehouse tuples into warehouse table
        sql_insert = """insert into warehouse (w_warehousekey, w_name,
                    w_capacity, w_suppkey, w_nationkey)
                    values(?,?,?,?,?)"""
        for w in warehouses:
            _conn.execute(sql_insert, w)


        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    sql = """select * from warehouse"""
    cur = _conn.cursor()
    cur.execute(sql)
    warehouses = cur.fetchall()

    header = '{:>10} {:<46} {:<4} {:>10} {:>10}'.format(
            'wId', 'wName', 'wCap', 'sId', 'nId'
        )
    print(header)
    with open("output/1.out", 'w') as out1:
        out1.write(header)
        out1.write('\n')
        for wh in warehouses:
            entry = '{:>10} {:<46} {:<4} {:>10} {:>10}'.format(
                wh[0], wh[1], wh[2], wh[3], wh[4]
            )
            print(entry)
            out1.write(entry)
            out1.write('\n')

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    sql_cap = """select n_name, count(w_name), sum(w_capacity) as ncap
            from warehouse, nation
            where w_nationkey = n_nationkey

            group by n_name
            order by ncap desc"""

    cur = _conn.cursor()
    cur.execute(sql_cap)
    nation_caps = cur.fetchall()
    header = '{:<46} {:<4} {:>10}'.format(
                'nation', 'numW', 'totCap'
            )

    with open("output/2.out", 'w') as out2:
        out2.write(f"{header}\n")
        for nat in nation_caps:
            entry = '{:<46} {:<4} {:>10}'.format(
                nat[0], nat[1], nat[2]
            )
            out2.write(f"{entry}\n")

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    sql = """SELECT s_name, n2.n_name, w_name
        from warehouse, supplier, nation as n1, nation as n2
        where w_suppkey = s_suppkey
        and n1.n_nationkey = w_nationkey
        and n2.n_nationkey = s_nationkey

        and n1.n_name = ? 
        order by s_name"""

    cur = _conn.cursor()
    header = '{:<20} {:<20} {:<40}'.format(
                'supplier', 'nation', 'warehouse'
            )

    with open("input/3.in", 'r') as infile:
        args = [line.rstrip() for line in infile]
    
    res = []
    with open("output/3.out", 'w') as out3:
        out3.write(f"{header}\n")
        for arg in args:
            cur.execute(sql, (arg,))
            res.append(cur.fetchall())
        for rows in res:
            for row in rows:
                print(row)
                entry = '{:<20} {:<20} {:<40}'.format(
                row[0], row[1], row[2]
                )
                out3.write(f"{entry}\n")


    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    sql = """select w_name, w_capacity
        from warehouse, region, nation
        where w_nationkey = n_nationkey
        and n_regionkey = r_regionkey
        and r_name = ?
        and w_capacity > ?
        order by w_capacity DESC"""

    with open("input/4.in", 'r') as infile:
        args = [line.rstrip() for line in infile]

    cur = _conn.cursor()
    cur.execute(sql, (args[0],args[1]))
    res = cur.fetchall()
    header = "{:<42} {:>8}".format("warehouse", "capacity")
    with open("output/4.out", 'w') as out4:
        out4.write(f"{header}\n")
        for line in res:
            entry = "{:<42} {:>8}".format(line[0], line[1])
            out4.write(f"{entry}\n")


    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    sql_regs = """select r_name from region
            order by r_name ASC"""
    cur = _conn.cursor()
    cur.execute(sql_regs)
    regs = cur.fetchall()

    sql = """select 
                r_name, 
                sum(w_capacity)
        from supplier, region, warehouse, nation as n1, nation as n2
        where w_nationkey = n1.n_nationkey
        and n1.n_regionkey = r_regionkey
        and s_nationkey = n2.n_nationkey
        and s_suppkey = w_suppkey

        and n2.n_name = ? -- 'UNITED STATES'
        group by r_name
        order by r_name"""

    with open("input/5.in", 'r') as infile:
        args = [line.rstrip() for line in infile]

    cur.execute(sql, (args[0],))
    res = cur.fetchall()
    print(res)
    print(regs)
    with open("output/5.out", 'w') as out5:
        header = "{:<32} {:>8}".format('region', 'capacity')
        out5.write(f"{header}\n")
        n = len(res)
        i = 0
        while i < n:
            if res[i][0] != regs[i][0]:
                res.insert(i, (regs[i][0], 0))
                n+=1
            entry = "{:<32} {:>8}".format(res[i][0], res[i][1])
            out5.write(f"{entry}\n")
            i+=1

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
