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

def insertWater(conn, id, cs):
    print(f"Inserting into water @id={id}")
    try:
        sql = "insert into Water_Quality (usgs_id, city_state) values (?,?)"
        args = [id, cs]
        conn.execute(sql, args)
        conn.commit()
        print("Success")
    except Error as err:
        conn.rollback()
        print(err)

def updateAQI(conn, loc, AQI, CO, pm10, pm25):
    print(f"Updating AQI @: {loc}")
    try:
        sql = f"""update AQI
            set AQI = ?,
            CO = ?,
            pm10 = ?,
            pm25 = ?
            where latitude like ? and longitude like ?
            """
        args = [AQI, CO, pm10, pm25, str(loc[0])+'%', str(loc[1])+'%']
        conn.execute(sql, args)
        conn.commit()
        print("Success")
    except Error as err:
        conn.rollback()
        print(err)


def deleteAQI(conn, key):
    print(f"Deleting AQI @: {loc}")
    sql = """delete from AQI
    where latitude like ? 
    and longitude like ?
    """
    try:
        conn.execute(sql, key)
        conn.commit()
        print("Success")
    except Error as err:
        conn.rollback()
        print(err)

if __name__ == "__main__":
    db = "cities.db"
    conn = openConnection(db)

    ''' USER USE CASE EXAMPLES '''
    
    print("\n# 1 find populous cities with good air quality")
    sql = """ select AQI.city_state
        from Cities_General, AQI
        where Cities_General.city_state = AQI.city_state
        and populations > ?
        and aqi < ?
        """
    args = [1000000, 50]
    queryDB(conn, sql, args)

    print("\n# 2 find cities with poor air quality, but low water magnesium content")
    sql = """ select AQI.city_state
        from Cities_General, AQI, Water_Quality
        where Cities_General.city_state = AQI.city_state
        and AQI.city_state = Water_Quality.city_state
        and hardness < ?
        and aqi > ?
        """
    args = [200, 80]
    queryDB(conn, sql, args)

    print("\n# 3 find the forecasted weather on the 4th day, in cities with a pop density > 4000")
    sql = """select fw.city_state, fw.current_temp, fw.description
    from Current_Weather as cw, Forecasted_Weather as fw, Cities_General as cg
    where cw.avg_coord = fw.avg_coord
    and cw.city_state = cg.city_state
    and weather_date_loc like ?
    and pop_density > ?
    """
    args = ['4%',4000]
    queryDB(conn, sql, args)

    print("\n# 4 show all major environment qualities of 5 given cities")
    sql  = """select cg.city_state, AQI, cw.current_temp, avg_ghi, fw.current_temp
    from Cities_General cg, AQI as aq, Current_Weather as cw, Forecasted_Weather as fw
    where cg.city_state = aq.city_state
    and aq.city_state = cw.city_state
    and cw.avg_coord = fw.avg_coord
    and cg.city_state = ?
    """
    locs = ['Sacramento,CA', 'New York,NY', 'Danbury,CT']
    for loc in locs:
        queryDB(conn, sql, (loc,))
    
    print("\n# 5 find cities with high robbery rates, but good air quality")
    sql = """select aq.city_state, robbery, aq.AQI
    from Cities_General as cg, Crime_Rates as cr, AQI as aq
    where aq.city_state = cg.city_state
    and cg.city_state = cr.city_state
    and robbery > ?
    and aq.AQI < ?
    """
    args = [30, 70]
    queryDB(conn, sql, args)

    print("\n# 6 find the total amount of arson cases in the 20 most populous cities, that are on the E/W coasts")
    sql = """select sum(distinct cr.arson)
    from Crime_Rates as cr, Cities_General as cg
    where cr.city_state = cg.city_state
    and cg.city_state not in (select cg2.city_state from Cities_General as cg2
                            where cg2.longitude > -115
                            and cg2.longitude < -82)
    order by populations desc
    limit 20;
    """
    queryDB(conn, sql)


    ''' BACK END USE CASE EXAMPLES '''

    print("\n# 7 USGS looks for cities that are missing hardness data, but have ph data")
    sql = """ select usgs_id
        from Water_Quality, Cities_General
        where Water_Quality.city_state = Cities_General.city_state
        and ph <> ''
        and hardness = ''
        """
    queryDB(conn, sql)

    print("\n# 8 AQI updates several locations")
    lat_lon = ((38.85,-77.05),(29.68,-95.29),(41.91,-87.72))
    updateAQI(conn, lat_lon[0], 38, 2.2, 19, 64)
    updateAQI(conn, lat_lon[1], 96, 4.9, 39, 112)
    updateAQI(conn, lat_lon[2], 12, 0.5, 9, 22)

    print("\n# 9 USGS adds new site for water testing")
    ids = ["USGS-58917539", "USGS-00589743"]
    city_states = ["Birdingham,AL", "Atlantis,GA"]
    for i in range(len(ids)):
        insertWater(conn, ids[i], city_states[i])

    print("\n# 10 AQI removes an incorrect forecast measurement")
    loc = ('38.2881%','-85.7413%')
    deleteAQI(conn, loc)


    closeConnection(conn, db)