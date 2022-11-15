import sqlite3
from sqlite3 import Error


def isaac_run_query(conn, sql, argument = []):
    print("Executing Query")
    try:
        cursor = conn.cursor()
        cursor.execute(sql, argument)

        table = cursor.fetchall()
        if len(table) == 0:
            print("No results from query execution")
        elif len(table) > 0:
            for row in table:
                print(row)
        
        print("success")
    except Error as e:
        conn.rollback()
        print(e)

def update_weather(conn, current_temp, wind, description, avg_dni, avg_ghi, avg_lat_tilt, city_state):
    print(f"Updating Weather: {city_state}")
    try:
        sql = f"""update Current_Weather
            set current_temp = ?,
            wind = ?,
            description = ?,
            avg_dni = ?,
            avg_ghi = ?,
            avg_lat_tilt = ?
            where city_state like ?
            """
        args = [current_temp, wind, description, avg_dni, avg_ghi, avg_lat_tilt, city_state + "%"]
        conn.execute(sql, args)
        conn.commit()
        print("Success: Weather Updated")
    except Error as e:
        conn.rollback()
        print(e)

def update_crime(conn, city_state, robbery, burglarly, violent_crime, arson):
    print(f"Updating Crimes: {city_state}")
    try:
        sql = f"""update Crime_Rates
            set robbery = ?,
            burglarly = ?,
            violent_crime = ?,
            arson = ?
            where city_state like ?
            """
        args = [robbery, burglarly, violent_crime, arson, city_state + "%"]
        conn.execute(sql, args)
        conn.commit()
        print("Success: Crime Updated")
    except Error as e:
        conn.rollback()
        print(e)

def update_weather_forecast(conn, weather_date_loc, current_temp, wind, description, city_state):
    print(f"Updating Weather Forecast: {city_state}")
    try:
        sql = f"""update Forecasted_Weather
            set current_temp = ?,
            wind = ?,
            description = ?
            where weather_date_loc like ?
            """
        args = [current_temp, wind, description, weather_date_loc + "%"]
        conn.execute(sql, args)
        conn.commit()
        print("Success: Weather Forecast Updated")
    except Error as e:
        conn.rollback()
        print(e)

if __name__ == "__main__":
    db = "cities.db"
    conn = sqlite3.connect(db) # open the connection to the data base

    """--For User--"""

    """NUMBER 11"""
    print("\n#11 Finds most violent city: highest violent-crimes")
    sql = """SELECT city_state, violent_crime
             FROM Crime_Rates 
             GROUP BY city_state
             ORDER BY burglarly DESC
             LIMIT ?"""
    args = [2]
    isaac_run_query(conn, sql, args)

    """ NUMBER 12"""
    print("\n#12 Finds the cities with the top 5 burgalaries")

    sql = """SELECT city_state, burglarly
             FROM Crime_Rates 
             GROUP BY city_state
             ORDER BY burglarly DESC
             LIMIT ?"""
    args = [6]
    isaac_run_query(conn, sql, args)

    """ NUMBER 13"""
    print("\n#13 Finds the cities with top 3 hottest temp and print number of arson crimes")

    sql = """SELECT c.city_state, arson, current_temp
             FROM Crime_Rates as c, Current_Weather as w
             WHERE c.city_state = w.city_state
             GROUP BY c.city_state
             ORDER BY current_temp DESC
             LIMIT ?"""
    args = [3]
    isaac_run_query(conn, sql, args)

    """ NUMBER 14"""
    print("\n#14 Finds current_weather, tomorrow's weather, current aqi, and avg_dni of given city")

    sql = """SELECT w.city_state, w.current_temp, f.current_temp, q.aqi, w.avg_dni
             FROM Forecasted_Weather as f, Current_Weather w, AQI as q
             WHERE f.avg_coord = w.avg_coord
             AND q.city_state = f.city_state
             AND f.weather_date_loc like ?
             AND w.city_state = ?
             """
    args = ["2%", "Los Angeles,CA"] # tomorrows weather, given city
    isaac_run_query(conn, sql, args)

    """ NUMBER 15"""
    print("\n#15 Finds the top 5 cities with the most violent-crimes with a pop > 300,000 in california")

    sql = """SELECT crime.city_state, crime.violent_crime, city.populations
             FROM Cities_General as city, Crime_Rates as crime
             WHERE city.city_state = crime.city_state
             AND city.populations > ?
             AND city.city_state like ?
             ORDER BY crime.violent_crime DESC
             LIMIT ?
             """
    args = [200000, "%,CA", 5]
    isaac_run_query(conn, sql, args)

    """ NUMBER 16"""
    print("\n#16 Finds cities that have the same aqi like Santa Barbara,CA")

    sql = """SELECT city.city_state, AQI.aqi
             FROM Cities_General as city, AQI
             WHERE city.city_state = AQI.city_state
             AND AQI.aqi = (SELECT sb_aqi.aqi 
                            FROM AQI as sb_aqi, Cities_General as sb
                            WHERE sb.city_state = sb_aqi.city_state
                            AND sb.city_state like ?)
             """
    args = ["Santa Barbara,CA"]
    isaac_run_query(conn, sql, args)

    """ NUMBER 17"""
    print("\n#17 Find the top 20 safest cities in the USA: Lowest burglaries, arson, violent-crime, and robbery. Then choose the city with the best water quaility ")

    sql = """SELECT cities, min(hard)
             FROM(
             SELECT city.city_state as cities, crime.robbery, crime.burglarly, crime.violent_crime, crime.arson, water.hardness as hard
             FROM Cities_General as city, Crime_Rates as crime, Water_Quality as water
             WHERE city.city_state  = crime.city_state
             AND city.city_state  = water.city_state
             ORDER BY crime.robbery, crime.burglarly, crime.violent_crime, crime.arson
             LIMIT ?)
             """
    args = [20]
    isaac_run_query(conn, sql, args)

    """-----BACK END----"""
    """NUMBER 18"""
    print("\n#18 update current weather/rads for a given city with a new weather/rads")
    update_weather(conn, 10, "wind is windy", "windy and cold", 5, 4, 3, "Santa Barbara,CA")
    
    """NUMBER 19"""
    print("\n#19 update crimes comitted for a given city")
    update_crime(conn, "Santa Barbara,CA", 5, 30, 0, 1)

    #checks to see if crime was updated in Santa Barbara,CA
    sql = """SELECT crime.city_state, crime.violent_crime, crime.arson, crime.burglarly, crime.robbery
             FROM Cities_General as city, Crime_Rates as crime
             WHERE city.city_state = crime.city_state
             AND city.city_state = ?
             """
    args = ["Santa Barbara,CA"]
    isaac_run_query(conn, sql, args)

    """Number 20"""
    print("\n#20 update weather forecast for a chosen day in a given city")
    update_weather_forecast(conn, "2,Santa Barbara,CA", 70, "still windy", "beach weather maybe", "Santa Barbara,CA")
    #checks to see if day 2 was updated in weather forecast for Santa Barbara
    sql = """SELECT city.city_state, f.current_temp, f.wind, f.description
             FROM Cities_General as city, Forecasted_Weather f
             WHERE city.city_state = f.city_state
             AND f.weather_date_loc = ?
             """
    args = ["2,Santa Barbara,CA"]
    isaac_run_query(conn, sql, args)
    #close the connection to the data base 
    conn.close()