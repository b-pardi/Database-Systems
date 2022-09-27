import requests
import pandas as pd
import sys

from key import key

#loc = input("Enter a city: ")
cities_df = pd.read_csv("data/uscities.csv")
loc = cities_df['city']

# air quality
air_dict = {'City':[], 'lat':[], 'long':[], 'Time Updated': [], 'AQI':[],
                'CO':[], 'H':[], 'NO2':[], 'Ozone':[], 'pm10':[], 'pm2.5':[]}

# 3 days out AQI forecast
air_forecast_dict = {'City':[], 'Time Updated':[], 'AQI':[], 'pm10':[], 'pm2.5':[]}

# weather
# other city info


'''
API has some data missing for some cities, function checks if data is available for each city,
and if it is appends it to the 'dest' dictionary.
'''
def tryAppend(dest_dict, dest_key, src_dict, src_keys):
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
    


# filling request and scraping API data for each city,
# putting into dictionary, then into dataframe
num_cities = 100
for i in range(num_cities):
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
        continue

    # takes json file from request, converts into dictionary
    air_data = r.json()['data']

    '''
    Appending data from AQI API for CURRENT air quality
    '''
    air_dict['City'].append(loc[i])
    tryAppend(air_dict, 'lat', air_data, ('city', 'geo', 0))
    tryAppend(air_dict, 'long', air_data, ('city', 'geo', 1))
    tryAppend(air_dict, 'Time Updated', air_data, ('time', 's'))
    tryAppend(air_dict, 'AQI', air_data, ('aqi',))

    # some cities, not all this information is available, explaining the try/except in function
    tryAppend(air_dict, 'CO', air_data, ('iaqi', 'co', 'v'))
    tryAppend(air_dict, 'H',  air_data, ('iaqi', 'h', 'v'))
    tryAppend(air_dict, 'NO2',  air_data, ('iaqi', 'no2', 'v'))
    tryAppend(air_dict, 'Ozone',  air_data, ('iaqi', 'o3', 'v'))
    tryAppend(air_dict, 'pm10', air_data, ('iaqi', 'pm10', 'v'))
    tryAppend(air_dict, 'pm2.5',  air_data, ('iaqi', 'pm25', 'v'))    


    '''
    Appending data from AQI API for 3 day FORECASTED air quality
    '''
    air_forecast_dict['City'].append(loc[i])
    tryAppend(air_forecast_dict, 'Time Updated', air_data, ('time', 's'))
    tryAppend(air_forecast_dict, 'AQI', air_data, ('aqi',))
    

    tryAppend(air_forecast_dict, 'pm10', air_data, ('forecast', 'daily', 'pm10', 5, 'avg'))
    tryAppend(air_forecast_dict, 'pm2.5', air_data, ('forecast', 'daily', 'pm25', 5, 'avg'))

aqi_df = pd.DataFrame(air_dict)
forecasted_aqi_df = pd.DataFrame(air_forecast_dict)
aqi_df.to_csv("data/aqi.csv", index=False)
forecasted_aqi_df.to_csv("data/forecasted_aqi.csv", index=False)
print(aqi_df.head())
print(forecasted_aqi_df.head())