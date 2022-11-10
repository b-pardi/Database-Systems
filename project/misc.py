import pandas as pd
import numpy as np
import random

def clean_gen():
    cities_df = pd.read_csv("data/uscities.csv")
    cities_df['city_state'] = cities_df['city'] + "," + cities_df['state_id']

    cities_df = cities_df[['city_state', 'county_name', 'population',
                    'density', 'lat', 'lng', 'timezone', 'zips']]

    cities_df = cities_df.drop_duplicates(['city_state'])

    cities_df.to_csv("data/uscities_scrubbed.csv", index=False)

# put lat/lon into columns of aqi table where na exists same way as cities
def add_aqi_na_cities():
    cities_df = pd.read_csv("data/uscities_scrubbed.csv")
    cities = cities_df['city_state'].values
    aqi_df = pd.read_csv("data/aqi.csv")
    aqi_nas = aqi_df[aqi_df['city_state'] == 'na'].index
    for na_index in aqi_nas:
        aqi_df.iloc[[na_index],[2]] = cities[na_index]
    print(aqi_df.tail())
    aqi_df.to_csv("data/aqi.csv", index=False)

def add_forecast_na_cities():
    cities_df = pd.read_csv("data/uscities_scrubbed.csv")
    cities = cities_df['city_state'].values
    forecast_df = pd.read_csv("data/forecasted_aqi.csv")
    forecast_nas = forecast_df[forecast_df['aqi_date_loc'] == 'na'].index
    for na_index in forecast_nas:
        prev_city = forecast_df.iloc[[na_index-1],[0]].values[0][0][2:]
        prev_city_index = np.where(cities == prev_city)[0]
        forecast_df.iloc[[na_index],[0]] = "0," + cities[prev_city_index+1]
    print(forecast_df.tail())
    forecast_df.to_csv("data/forecasted_aqi.csv", index=False)

def camel_case(str):
    if str == 'na':
        return 'na'

    try: 
        city, state = str.split(',')
    except:
        return('na')
    city = city.lower().split()
    city = [str.capitalize() for str in city]
    city = ' '.join(city)
    city_state = city + ',' + state
    print (city_state)
    return city_state
    

def camel_case_data(file, col):
    water_df = pd.read_csv(file)
    city_states = water_df[col].values
    city_states = [camel_case(loc) for loc in city_states]
    water_df[col] = city_states
    print(water_df.tail())
    water_df.to_csv(file, index=False)

def drop_rows(file, col, condition):
    df = pd.read_csv(file)
    df = df[df[col].str.contains(condition)==False]
    print(df.head())
    df.to_csv(file, index=False)



def make_lat_lon_unique(file, col):
    df = pd.read_csv(file)
    lat_lon = df[col].values
    coord_split = []
    for coord in lat_lon:
        lat, lon = coord.split(',')
        coord_split.append([lat, lon])
    #print(coord_split)

    temp = 0
    for coord in coord_split:
        dups = [elem for elem in coord_split if elem == coord]
        temp +=1

def drop_dups(file, col):
    df = pd.read_csv(file)
    df = df.drop_duplicates(col)
    df.to_csv(file, index=False)
    
if __name__ == "__main__":
    #clean_gen()
    #add_aqi_na_cities()
    #add_forecast_na_cities()
    #camel_case_data("data/org_water_updated.csv", 'city_state')
    #drop_rows("data/weather_and_solar.csv",'avg_coord', 'n/a')
    #drop_dups("data/crime.csv", 'city_state')