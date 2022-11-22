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

def dropViews(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop views")

    views = (('V1'), ('V2'), ('V5'), ('V10'), ('V151'), ('V152'))

    try:
        for view in views:
            sql = "DROP view if exists " + view
            _conn.execute(sql)
            print(f"dropped: {view}")
        print("success")
    except Error as exc:
        _conn.rollback()
        print(exc)

    print("++++++++++++++++++++++++++++++++++")

def create_View1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")
    sqlV1 = """create view V1(c_custkey, c_name, c_address, c_phone, c_acctbal,
            c_mktsegment, c_comment, c_nation, c_region) as 
                select c_custkey, c_name, c_address, c_phone, c_acctbal,
                c_mktsegment, c_comment, n_name, r_name
                from customer, nation, region
                where c_nationkey = n_nationkey
                and n_regionkey = r_regionkey;
            """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV1)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")

    sqlV2 = """create view V2(s_suppkey, s_name, s_address, s_phone,
                s_acctbal, s_comment, s_nation, s_region) as
                    select s_suppkey, s_name, s_address, s_phone,
                    s_acctbal, s_comment, n_name, r_name
                    from supplier, nation, region
                    where s_nationkey = n_nationkey
                    and n_regionkey = r_regionkey;
                    """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV2)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def create_View5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V5")

    sqlV5 = """create view V5(o_orderkey, o_custkey, o_orderstatus, o_totalprice,
            o_orderyear, o_orderpriority, o_clerk, o_shippriority, o_comment) AS
                select o_orderkey, o_custkey, o_orderstatus, o_totalprice,
                substr(o_orderdate, 1, 4), o_orderpriority, o_clerk, o_shippriority, o_comment
                from orders;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV5)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")

    sqlV10 = """create view V10(p_type, min_discount, max_discount) AS
                    select p_type, min(l_discount), max(l_discount)
                    from lineitem, part
                    where l_partkey = p_partkey
                    group by p_type;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV10)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def create_View151(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V151")

    sqlV151 = """create view V151(c_custkey, c_name, c_nationkey, c_acctbal) as
                select c_custkey, c_name, c_nationkey, c_acctbal
                from customer
                where c_acctbal > 0;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV151)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def create_View152(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V152")

    sqlV152 = """create view V152(s_suppkey, s_name, s_nationkey, s_acctbal) as
                select s_suppkey, s_name, s_nationkey, s_acctbal
                from supplier
                where s_acctbal < 0;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sqlV152)
        _conn.commit()
        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    sql = """select c_name, sum(o_totalprice)
            from V1, orders
            where o_custkey = c_custkey
            and c_nation = "FRANCE"
            and o_orderdate LIKE '1995%'
            group by c_name;
        """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/1.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{round(row[1],2)}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    sql = """select s_region, count(*)
            from V2
            group by s_region;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/2.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    sql = """select c_nation, count(*)
            from orders, V1
            where c_custkey = o_custkey
            and c_region = 'AMERICA'
            group by c_nation;
            """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/3.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    sql = """select s_name, count(ps_partkey)
            from partsupp, V2, part
            where p_partkey = ps_partkey
            and ps_suppkey = s_suppkey
            and s_nation = 'CANADA'
            and p_size < 20
            group by s_name;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/4.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    sql = """select c_name, count(*)
            from V5, V1
            where o_custkey = c_custkey
            and c_nation = 'GERMANY'
            and o_orderyear = '1993'
            group by c_name;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/5.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    sql = """select s_name, o_orderpriority, count(distinct ps_partkey)
            from V5, partsupp, lineitem, V2
            where l_orderkey = o_orderkey
            and l_partkey = ps_partkey
            and l_suppkey = ps_suppkey
            and ps_suppkey = s_suppkey
            and s_nation = 'CANADA'
            group by s_name, o_orderpriority;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/6.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}|{row[2]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)    

    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    sql = """select c_nation, o_orderstatus, count(*)
            from V1, V5
            where o_custkey = c_custkey
            and c_region = 'AMERICA'
            group by c_nation, o_orderstatus;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/7.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}|{row[2]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)   

    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")

    sql = """select s_nation, count(distinct l_orderkey) as co
            from V2, V5, lineitem
            where o_orderkey = l_orderkey
            and l_suppkey = s_suppkey
            and o_orderstatus = 'F'
            and o_orderyear = '1995'
            group by s_nation
            having co > 50;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/8.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    sql = """select count(distinct o_clerk)
            from V5, V2, lineitem
            where o_orderkey = l_orderkey
            and l_suppkey = s_suppkey
            and s_nation = 'UNITED STATES';
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/9.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    sql = """select p_type, min_discount, max_discount
            from V10
            where p_type like '%ECONOMY%'
            and p_type like '%COPPER%'
            group by p_type;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/10.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}|{row[2]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    sql = """select s1.s_region, s1.s_name, s1.s_acctbal
            from V2 s1
            where s1.s_acctbal = (select max(s2.s_acctbal) 
                            from V2 s2
                            where s1.s_region = s2.s_region
                            )
            order by s_region;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/11.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}|{row[2]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    sql = """select s_nation, max(s_acctbal) as mb
        from V2
        group by s_nation
        having mb > 9000;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/12.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    sql = """select count(*)
            from V5, V2, V1, lineitem
            where o_orderkey = l_orderkey
            and o_custkey = c_custkey
            and l_suppkey = s_suppkey
            and s_region = 'AFRICA'
            and c_nation = 'UNITED STATES';
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/13.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    sql = """select s_region, c_region, max(o_totalprice)
            from lineitem, V1, V2, V5
            where l_suppkey = s_suppkey
            and l_orderkey = o_orderkey
            and o_custkey = c_custkey
            group by s_region, c_region;
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/14.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}|{row[1]}|{row[2]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    sql = """select count(distinct l_orderkey)
            from lineitem, V152, orders, V151
            where l_suppkey = s_suppkey
            and l_orderkey = o_orderkey
            and o_custkey = c_custkey
    """

    try:
        cur = _conn.cursor()
        cur.execute(sql)

        res = cur.fetchall()
        with open("output/15.out", 'w') as out:
            for row in res:
                entry = f"{row[0]}\n"
                out.write(entry)

        print("success")
    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropViews(conn)
        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)
        Q4(conn)

        create_View5(conn)
        Q5(conn)

        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)

        create_View151(conn)
        create_View152(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
