import pandas as pd
import numpy as np
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

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

def add_keys_col(file, new_col_name):
    df = pd.read_csv(file)
    length = df.shape[0]
    df.insert(0, new_col_name, [i for i in range(1,length+1)])
    print(df.head())
    print(df.tail())
    df.to_csv(file, index=False)

def add_foreign_keys_col(dest_file, foreign_file, foreign_key_col_name, foreign_attribute, shared_id):
    df1 = pd.read_csv(dest_file)
    df2 = pd.read_csv(foreign_file)

    df3 = df1.merge(df2[[foreign_key_col_name, foreign_attribute, shared_id]], on=shared_id, how='left')
    df3.to_csv(dest_file, index=False)
    print(df3.head())

    #df1.insert(0, foreign_key_col_name, foreign_keys)

def build_bridge(file1, file2, key1, key2, shared_id, dest_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = df1[[key1,shared_id]].merge(df2[[key2,shared_id]], on=shared_id, how='left')
    df3.insert(0, 'b_id', [i for i in range(1,df3.shape[0]+1)])
    df3.to_csv(dest_file, index=False)
    print(df3.head())

def dup_water_rows(file, unique_col, key_col, num_dups):
    df = pd.read_csv(file)
    ids = df[unique_col].values
    length = df.shape[0]
    rands = random.sample(range(1,length-1), num_dups)
    for i, r in enumerate(rands):
        row = df.iloc[r]
        row[key_col] = i + 1 + length
        monitor = "USGS-" + str(random.randint(10000000, 99999999))
        row[unique_col] = monitor
        df = df.append(row)
    df = df.reset_index(drop=True)
    print(df.tail())

    df.to_csv(file, index=False)

def insert_state_key(dest_file, src_file):
    df1 = pd.read_csv(dest_file)
    df2 = pd.read_csv(src_file)
    df1['state_abbrev'] = df1['city_state'].apply(lambda row: row[-2:])
    df3 = df1.merge(df2[['s_key', 'state_abbrev']], on='state_abbrev', how='inner')
    print(df3[['cs_key','city_state','s_key','state_abbrev']].head())
    df3['s_key'] = df3['s_key'].astype(int)
    df3 = df3.sort_values(by=['cs_key'])
    df3.to_csv(dest_file, index=False)
   

def rewrite_forecasted_aqi():
    df1 = pd.read_csv("data/aqi.csv")
    df2 = pd.read_csv("data/forecasted_aqi.csv")

    for i in range(df1.shape[0]):
        row = df1.iloc[i]
        row = row[['aqi_key', 'time_updated', 'Ozone', 'pm10', 'pm25']]
        row['f_aqi_key'] = 5*i
        f_row_dict = row.to_dict()
        for j in range(5):
            f_row_dict['aqi_key'] = [i + 1]
            f_row_dict['f_aqi_key'] = [((i+1) * 5) + j]
            f_row_dict['o3'] = [(random.randint(3,20))]
            f_row_dict['pm10'] = [(random.randint(8,60))]
            f_row_dict['pm25'] = [(random.randint(20,125))]
            f_row = pd.DataFrame.from_dict(f_row_dict)
            #print(f_row.head())
            df2 = df2.append(f_row)
    df2.to_csv("data/forecasted_aqi.csv")

    print(df2.head())


if __name__ == "__main__":
    #clean_gen()
    #add_aqi_na_cities()
    #add_forecast_na_cities()
    #camel_case_data("data/org_water_updated.csv", 'city_state')
    #drop_rows("data/weather_and_solar.csv",'avg_coord', 'n/a')
    drop_dups("data/uscities_scrubbed.csv", 'cs_key')
    #add_keys_col("data/states.csv", "s_key")
    #add_foreign_keys_col("data/uscities_scrubbed.csv", "data/org_water_updated.csv", "usgs_key", "MonitoringLocationIdentifier", "city_state")
    #build_bridge("data/uscities_scrubbed.csv", "data/org_water_updated.csv",'cs_key', 'usgs_key', 'city_state', "data/cities_water_bridge.csv")
    #dup_water_rows("data/org_water_updated.csv", 'MonitoringLocationIdentifier', 'usgs_key', 150)
    #insert_state_key("data/uscities_scrubbed.csv", "data/states.csv")
    #rewrite_forecasted_aqi()