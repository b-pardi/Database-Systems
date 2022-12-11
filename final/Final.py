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


def build_data_cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("BUILD DATA CUBE")

    cur = _conn.cursor()
    sql = '''
    INSERT INTO price_cube

    -- ALL
    select 'ALL' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
    from distributor

    union

    select
        -- determine distributor
        CASE
            when 1
            then 
                'ALL'
        end distributor_type,
        -- determine product type
        CASE
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'laptop')
            THEN
                'laptop'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'pc')
            THEN
                'pc'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'printer')
            THEN
                'printer'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and (product.type = 'printer'
                    or product.type = 'laptop'
                    or product.type = 'pc'))
            THEN
                'ALL'
            end product_type,
        
        -- count appropriately
        count(distributor.model) as num_prod,

        -- sum appropriately
        sum(distributor.price) as tot_price

    from distributor
    group by distributor_type, product_type

    union

    -- distributors
    select 'distributor' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
    from distributor
    where distributor.name not in (select product.maker from product)

    union

    select
        -- determine distributor
        CASE
            when distributor.name not in
                (select product.maker from product)
            then 
                'distributor'
        end distributor_type,
        
        -- determine product type
        CASE
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'laptop')
            THEN
                'laptop'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'pc')
            THEN
                'pc'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'printer')
            THEN
                'printer'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and (product.type = 'printer'
                    or product.type = 'laptop'
                    or product.type = 'pc'))
            THEN
                'ALL'
            end product_type,
        
        -- count appropriately
        CASE
            when distributor.name not in
                (select product.maker from product)
            then count(distributor.model)
        end num_prod,

        -- sum appropriately
        CASE
            when distributor.name not in
                (select product.maker from product)
            then sum(distributor.price)
        end tot_price

    from distributor

    where distributor.name not in (select product.maker from product)

    group by distributor_type, product_type

    union

    -- producer
    select 'producer' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
    from distributor
    where distributor.name in (select product.maker from product)

    union

    SELECT
        CASE
        when distributor.name in
                (select product.maker from product)
            then 
                'producer'
        end distributor_type,
        -- determine product type
        CASE
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'laptop')
            THEN
                'laptop'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'pc')
            THEN
                'pc'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and product.type = 'printer')
            THEN
                'printer'
            when distributor.model IN
                (select product.model
                from product, distributor
                where product.model = distributor.model
                and (product.type = 'printer'
                    or product.type = 'laptop'
                    or product.type = 'pc'))
            THEN
                'ALL'
            end product_type,
        
        -- count appropriately
        CASE
            when distributor.name in
                (select product.maker from product)
            then count(distributor.model)
        end num_prod,

        -- sum appropriately
        CASE
            when distributor.name in
                (select product.maker from product)
            then sum(distributor.price)
        end tot_price

    from distributor
    where distributor.name in (select product.maker from product)
    group by distributor_type, product_type

        
    '''
    try:
        cur = _conn.cursor()
        cur.execute(sql)

    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")


def print_Product(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT PRODUCT")

    try:
        cur = _conn.cursor()
        cur.execute("SELECT * FROM Product")
        rows = cur.fetchall()
    except Error as err:
        _conn.rollback()
        print(err)

    l = '{:<20} {:<20} {:<20}'.format("model", "type", "maker")
    print(l)

    for row in rows:
        print('{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2]))

    print("++++++++++++++++++++++++++++++++++")


def print_Distributor(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DISTRIBUTOR")

    try:
        cur = _conn.cursor()
        cur.execute("SELECT * FROM distributor")
        rows = cur.fetchall()
    except Error as err:
        _conn.rollback()
        print(err)

    l = '{:<20} {:<20} {:>20}'.format("model", "name", "price")
    print(l)

    for row in rows:
        # make into list not tuples since lists are mutable
        row = list(row)
        for i in range(len(row)):
            if row[i] == None:
                row[i] = 'NULL'
        print('{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2]))

    print("++++++++++++++++++++++++++++++++++")


def print_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DATA CUBE")

    l = '{:<20} {:<20} {:>10} {:>10}'.format("dist", "prod", "cnt", "total")
    print(l)

    try:
        cur = _conn.cursor()
        cur.execute("SELECT * FROM price_cube")
        rows = cur.fetchall()
    except Error as err:
        _conn.rollback()
        print(err)

    for row in rows:
        print('{:<20} {:<20} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3]))

    print("++++++++++++++++++++++++++++++++++")


def modifications(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("MODIFICATIONS")

    

    with open('modifications.txt', 'r') as mod_file:
        mods = [line.rstrip() for line in mod_file]
    
    try:
        cur = _conn.cursor()
        for mod in mods:
            table = mod[0]
            op = mod[1]
            model = mod[2]
            if table == "Product":
                if op == 'I':
                    print('insert product')
                    prod_type = mod[3]
                    maker = mod[4]
                    sql = '''insert into product (model, type, maker)
                        values (?,?,?);
                        insert into distributor (model, name, price)
                        values (?,?,'NULL')
                        '''
                    args = [model, prod_type, maker, model, maker]

                    cur.execute(sql, args)
                    _conn.commit()

                elif op == 'D':
                    print('delte product')
                    sql = '''delete from distributor where model = ?'''
                    cur.execute(sql, (model,))
                    _conn.commit()

            elif table == "Distributor":
                name = mod[3]
                if op == 'I':
                    print('insert dist')
                    price = mod[4]
                    sql = '''insert into distributor (model, name, price)
                        values (?,?,?)
                        '''
                    args = [model, name, price]
                    cur.execute(sql, args)
                    _conn.commit()                    

                elif op == 'D':
                    print('delte dist')
                    sql = '''update distributor where model = ? and name = ?
                    set price = 'NULL'
                    '''
                    args = [model, name]
                    cur.execute(sql, args)
                    _conn.commit() 

        # reset data cube
        sql = '''delete from price_cube
            '''
        cur.execute(sql)
        _conn.commit
        build_data_cube(_conn)

    except Error as err:
        _conn.rollback()
        print(err)

    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        print_Product(conn)
        print_Distributor(conn)

        build_data_cube(conn)
        print_Cube(conn)

        modifications(conn)

        print_Product(conn)
        print_Distributor(conn)
        print_Cube(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
