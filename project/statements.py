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
        
        rows = cur.fetchall()
        if len(rows) == 0:
            print("No results matched query")
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


def deleteDB(sql, conn):
    pass

if __name__ == "__main__":
    db = "cities.db"
    conn = openConnection(db)

    ''' USER USE CASE EXAMPLES '''
    
    # 1 find populous cities with good air quality
    sql = """ select AQI.city_state
        from Cities_General, AQI
        where Cities_General.city_state = AQI.city_state
        and populations > ?
        and aqi < ?
        """
    args = [1000000, 50]
    queryDB(conn, sql, args)

    # 2 find cities with poor air quality, but low water magnesium content
    sql = """ select AQI.city_state
        from Cities_General, AQI, Water_Quality
        where Cities_General.city_state = AQI.city_state
        and AQI.city_state = Water_Quality.city_state
        and hardness < ?
        and aqi > ?
        """
    args = [200, 80]
    queryDB(conn, sql, args)
    

    ''' BACK END USE CASE EXAMPLES '''

    # 7 USGS looks for cities that are missing hardness data, but have ph data
    # fiz water table we dont want all caps for city_state
    sql = """ select usgs_id
        from Water_Quality, Cities_General
        where Water_Quality.city_state = Cities_General.city_state
        and ph <> ''
        and hardness = ''
        """
    queryDB(conn, sql)

    # 8 AQI updates several locations
    lat_lon = ((38.85,-77.05),(29.68,-95.29),(41.91,-87.72))
    updateAQI(conn, lat_lon[0], 38, 2.2, 19, 64)
    updateAQI(conn, lat_lon[1], 96, 4.9, 39, 112)
    updateAQI(conn, lat_lon[2], 12, 0.5, 9, 22)

    # 9 USGS adds new site for water testing
    ids = ["USGS-58917539", "USGS-00589743"]
    city_states = ["Birdingham,AL", "Atlantis,GA"]
    for i in range(len(ids)):
        insertWater(conn, ids[i], city_states[i])


    # 10 USGS updates values of newly added sites


    # 11 AQI removes an incorrect forecast measurement


    # 12 AQI updates cities air quality data
    
    closeConnection(conn, db)