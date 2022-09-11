-- SQLite

--Run these commands in the .sqlite3 terminal.
.mode "csv"
.separator ","
.headers off
--replace the file path with your path
.import '| tail -n +2 cal_cities_lat_long.csv' Cities_Loc
.import '| tail -n +2 cal_populations_city.csv' Cities_Population
