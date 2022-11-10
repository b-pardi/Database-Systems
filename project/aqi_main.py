import requests
import pandas as pd
import sys

from key import key

#loc = input("Enter a city: ")
cities_df = pd.read_csv("data/uscities_scrubbed.csv")
city_state = cities_df['city_state'].values
# get only city from city state
loc = [city[:-3] for city in city_state]

# air quality
air_dict = {'latitude':[], 'city_state':[], 'city_state':[], 'time_updated': [], 'AQI':[],
                'CO':[], 'H':[], 'NO2':[], 'Ozone':[], 'pm10':[], 'pm25':[]}

# 3 days out AQI forecast
air_forecast_dict = {'aqi_date_loc':[], 'time_updated':[], 'o3':[], 'pm10':[], 'pm25':[]}



'''
API has some data missing for some cities, function checks if data is available for each city,
and if it is appends it to the 'dest' dictionary.
'''
def tryAppendAQI(dest_dict, dest_key, src_dict, src_keys):
    i = 1
    data = src_dict[src_keys[0]]
    while i < len(src_keys):
        if src_keys != None:
            try:
                data = data[src_keys[i]]
            except:
                data = 'na'
        i+=1

    # checks to make sure data is only 1 item, not a dictionary
    # data will be not a dict if the data sought after is available
    if not isinstance(data, dict):
        dest_dict[dest_key].append(data)
    
def tryAppendAQIForecast(dest_dict, dest_key, src_dict, src_keys):
    i = 1
    data = src_dict[src_keys[0]]
    while i < len(src_keys):
        if src_keys != None:
            try:
                data = data[src_keys[i]]
            except:
                data = 'na'
                print(f"**{data} unavailable for city**")
        i+=1
    
    if not isinstance(data, dict):
        dest_dict[dest_key].append(data)

# filling request and scraping API data for each city,
# putting into dictionary, then into dataframe
num_cities = len(city_state)
for i in range(num_cities):
    print(city_state[i])
    try:
        # send API request
        r = requests.get(f"https://api.waqi.info/feed/{loc[i]}/?token={key}")
    except requests.exceptions.InvalidSchema:
        # check request succesfully received
        print("Connection failed! Check the URL")
        sys.exit(1)

    # check if entered city is valid
    if r.json()['data'] == "Unknown station":
        print(f"Invalid Location: {loc[i]}")
        for key1 in air_dict:
            if key1 == 'City':
                air_dict[key1].append(loc[i])
            else:
                air_dict[key1].append('na')
        for key2 in air_forecast_dict:
            if key2 == 'City':
                air_forecast_dict[key2].append(loc[i])
            else:
                air_forecast_dict[key2].append('na')
        continue

    # takes json file from request, converts into dictionary
    air_data = r.json()['data']

    '''
    Appending data from AQI API for CURRENT air quality
    '''
    air_dict['city_state'].append(city_state[i])
    tryAppendAQI(air_dict, 'latitude', air_data, ('city', 'geo', 0))
    tryAppendAQI(air_dict, 'longitude', air_data, ('city', 'geo', 1))
    tryAppendAQI(air_dict, 'time_updated', air_data, ('time', 's'))
    tryAppendAQI(air_dict, 'AQI', air_data, ('aqi',))

    # some cities, not all this information is available, explaining the try/except in function
    tryAppendAQI(air_dict, 'CO', air_data, ('iaqi', 'co', 'v'))
    tryAppendAQI(air_dict, 'H',  air_data, ('iaqi', 'h', 'v'))
    tryAppendAQI(air_dict, 'NO2',  air_data, ('iaqi', 'no2', 'v'))
    tryAppendAQI(air_dict, 'Ozone',  air_data, ('iaqi', 'o3', 'v'))
    tryAppendAQI(air_dict, 'pm10', air_data, ('iaqi', 'pm10', 'v'))
    tryAppendAQI(air_dict, 'pm25',  air_data, ('iaqi', 'pm25', 'v'))    


    '''
    Appending data from AQI API for FORECASTED air quality
    '''
    # forecast section contains 3 past days as well, ignore those
    try:
        num_days = len(air_data['forecast']['daily']['pm10'])
    except KeyError as ke:
        print("**forecast N/A**")
        num_days = 0

    for day_count in range(3, num_days):
        air_forecast_dict['aqi_date_loc'].append(str(day_count-2) + ',' + city_state[i])
        tryAppendAQI(air_forecast_dict, 'time_updated', air_data, ('time', 's'))
        tryAppendAQI(air_forecast_dict, 'o3', air_data, ('forecast', 'daily', 'o3', day_count, 'avg'))
        tryAppendAQI(air_forecast_dict, 'pm10', air_data, ('forecast', 'daily', 'pm10', day_count, 'avg'))
        tryAppendAQI(air_forecast_dict, 'pm25', air_data, ('forecast', 'daily', 'pm25', day_count, 'avg'))

print(air_forecast_dict)
aqi_df = pd.DataFrame(air_dict)
forecasted_aqi_df = pd.DataFrame(air_forecast_dict)
aqi_df.to_csv("data/aqi.csv", index=False)
forecasted_aqi_df.to_csv("data/forecasted_aqi.csv", index=False)
print(aqi_df.head())
print(forecasted_aqi_df.head())