import requests
import pandas as pd
import sys

from key import key

#loc = input("Enter a city: ")
cities_df = pd.read_csv("uscities.csv")
loc = cities_df['city']

# air quality
air_dict = {'City':[], 'lat':[], 'long':[], 'Time Updated': [], 'AQI':[],
                'CO':[], 'H':[], 'NO2':[], 'Ozone':[], 'pm10':[], 'pm2.5':[]}

# 3 days out AQI forecast
air_forecast_dict = {'City':[], 'Time Updated':[], 'AQI':[], 'pm10':[], 'pm2.5':[]}

# weather
# other city info


# filling request and scraping API data for each city,
# putting into dictionary, then into dataframe
for i in range(9):
    try:
        # send API request
        r = requests.get(f"https://api.waqi.info/feed/{loc[i]}/?token={key}")
    except requests.exceptions.InvalidSchema:
        # check request succesfully received
        print("Connection failed! Check the URL")
        sys.exit(1)

    # check if entered city is valid
    if r.json()['data'] == "Unknown station":
        print("Invalid Location")
        sys.exit(1)

    # takes json file from request, converts into dictionary
    air_data = r.json()['data']

    '''
    Appending data from AQI API for CURRENT air quality
    '''
    air_dict['City'].append(loc[i])
    air_dict['lat'].append(air_data['city']['geo'][0])
    air_dict['long'].append(air_data['city']['geo'][1])
    air_dict['Time Updated'].append(air_data['time']['s'])
    air_dict['AQI'].append(air_data['aqi'])

    # some cities, not all this information is available
    try:
        air_dict['CO'].append(air_data['iaqi']['co']['v'])
    except:
        air_dict['CO'].append('na')
    try:
        air_dict['H'].append(air_data['iaqi']['h']['v'])
    except:
        air_dict['H'].append('na')
    try:
        air_dict['NO2'].append(air_data['iaqi']['no2']['v'])
    except:
        air_dict['NO2'].append('na')
    try:
        air_dict['Ozone'].append(air_data['iaqi']['o3']['v'])
    except:
        air_dict['Ozone'].append('na')
    try:
        air_dict['pm10'].append(air_data['iaqi']['pm25']['v'])
    except:
        air_dict['pm10'].append('na')
    try:
        air_dict['pm2.5'].append(air_data['iaqi']['pm25']['v'])
    except:
        air_dict['pm2.5'].append('na')


    '''
    Appending data from AQI API for 3 day FORECASTED air quality
    '''
    air_forecast_dict['City'].append(loc[i])
    air_forecast_dict['Time Updated'].append(air_data['time']['s'])
    air_forecast_dict['AQI'].append(air_data['aqi'])
    try:
        air_forecast_dict['pm10'].append(air_data['iaqi']['pm25']['v'])
    except:
        air_forecast_dict['pm10'].append('na')
    try:
        air_forecast_dict['pm2.5'].append(air_data['iaqi']['pm25']['v'])
    except:
        air_forecast_dict['pm2.5'].append('na')


aqi_df = pd.DataFrame(air_dict)
forecasted_aqi_df = pd.DataFrame(air_dict)
print(aqi_df.head())
print(forecasted_aqi_df.head())