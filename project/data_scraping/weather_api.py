import requests
import json
import pandas as pd
import time
# reads unscrubbed uscities.csv file and grabs the longitude and latitude of
# each city 
# city_name, latitude, longitude
cities_df = pd.read_csv("data/uscities_scrubbed.csv")
latitude = cities_df['lat']
longitude = cities_df['lng']
city_name = cities_df['city_state']

# current weather and weather forcast dictionaries

current_weathers_dic = {'avg_coord':[],'x_y_grid_pt':[], 'city_state':[], 'current_temp':[], 'wind': [],
                'description':[]}

weather_forecast_dic = {'weather_date_loc':[], 'avg_coord':[], 'city_state':[], 'temperature':[], 'wind':[], 'description':[]}

# loops through the cities and grabs their weather forecast using cities latitude and longitude to get a gridpoint_endpoint.
# gridpoint_endpoint is then used to get temperature of the grid 
number_city = len(cities_df)
file = open('data/weather.txt', 'a')
for i in range(0,number_city):
    # break from while loop only if code succeeds if KeyError caught then continue while loop
    rc1 =0
    rc2 = 0
    # continue to while loop until data is collected 
    while True:
        try:
            grid_endpoint = requests.get(f'https://api.weather.gov/points/{latitude[i]},{longitude[i]}')

            # if error then try 5 more times then break 
            if grid_endpoint.status_code != 200:
                rc1 +=1
                time.sleep(0.5)
                if rc1 >5:
                    print(city_name[i]) 
                    # append n/a for current_weather for these cases before break
                    current_weathers_dic['avg_coord'].append("n/a")
                    current_weathers_dic['x_y_grid_pt'].append("n/a")
                    current_weathers_dic['city_state'].append(city_name[i])
                    current_weathers_dic['current_temp'].append("n/a")
                    current_weathers_dic['wind'].append("n/a")
                    current_weathers_dic['description'].append("n/a")

                    # append n/a for weather_forecast for these cases before break
                    weather_forecast_dic['weather_date_loc'].append("n/a")
                    weather_forecast_dic['avg_coord'].append("n/a")
                    weather_forecast_dic['city_state'].append(city_name[i])
                    weather_forecast_dic['temperature'].append("n/a")
                    weather_forecast_dic['wind'].append("n/a")
                    weather_forecast_dic['description'].append("n/a")
                    break
            grid_x = grid_endpoint.json()['properties']['gridX']
            grid_y = grid_endpoint.json()['properties']['gridY']
            grid_Id = grid_endpoint.json()['properties']['gridId']

            forecast = requests.get(f'https://api.weather.gov/gridpoints/{grid_Id}/{grid_x},{grid_y}/forecast')

            # if error pops up then try 5 more times then break after and continue 
            if forecast.status_code != 200:
                rc2 +=1
                time.sleep(0.5)
                if rc2 >5:
                    print(city_name[i]) 
                    # append n/a for these cases before break
                    current_weathers_dic['avg_coord'].append("n/a")
                    current_weathers_dic['x_y_grid_pt'].append("n/a")
                    current_weathers_dic['city_state'].append(city_name[i])
                    current_weathers_dic['current_temp'].append("n/a")
                    current_weathers_dic['wind'].append("n/a")
                    current_weathers_dic['description'].append("n/a")

                    # append n/a for these cases before break
                    weather_forecast_dic['weather_date_loc'].append("n/a")
                    weather_forecast_dic['avg_coord'].append("n/a")
                    weather_forecast_dic['city_state'].append(city_name[i])
                    weather_forecast_dic['temperature'].append("n/a")
                    weather_forecast_dic['wind'].append("n/a")
                    weather_forecast_dic['description'].append("n/a")
                    break
            
            # grabs weather and weather forecast data 
            current_weather = forecast.json()['properties']['periods'][0]['temperature']
            day2_weather = forecast.json()['properties']['periods'][1]['temperature']
            day3_weather = forecast.json()['properties']['periods'][2]['temperature']
            day4_weather = forecast.json()['properties']['periods'][3]['temperature']
            day5_weather = forecast.json()['properties']['periods'][4]['temperature']

            description = forecast.json()['properties']['periods'][0]['shortForecast']
            description_2 = forecast.json()['properties']['periods'][1]['shortForecast']
            description_3 = forecast.json()['properties']['periods'][2]['shortForecast']
            description_4 = forecast.json()['properties']['periods'][3]['shortForecast']
            description_5 = forecast.json()['properties']['periods'][4]['shortForecast']

            wind_speed = forecast.json()['properties']['periods'][0]['windSpeed']
            wind_speed_2 = forecast.json()['properties']['periods'][1]['windSpeed']
            wind_speed_3 = forecast.json()['properties']['periods'][2]['windSpeed']
            wind_speed_4 = forecast.json()['properties']['periods'][3]['windSpeed']
            wind_speed_5 = forecast.json()['properties']['periods'][4]['windSpeed']

            # "x, y"
            x_y = f"{grid_x}" + ", " + f"{grid_y}"

            # avg_coord
            average_coordinate = (latitude[i] + longitude[i]) / 2

            # append data to weather_forecast 5 times for 5-day forecast
            temperature_forecast_list = [current_weather, day2_weather, day3_weather, day4_weather, day5_weather]
            wind_speed_forecast_list = [wind_speed, wind_speed_2, wind_speed_3, wind_speed_4, wind_speed_5]
            description_forecast_list = [description, description_2, description_3, description_4, description_5]
            for j in range(0,5):
                weather_date_location = str(j + 1) + "," + city_name[i] #unique key for each city 

                weather_forecast_dic['weather_date_loc'].append(weather_date_location)
                weather_forecast_dic['avg_coord'].append(average_coordinate)
                weather_forecast_dic['city_state'].append(city_name[i])
                weather_forecast_dic['temperature'].append(temperature_forecast_list[j])
                weather_forecast_dic['wind'].append(wind_speed_forecast_list[j])
                weather_forecast_dic['description'].append(description_forecast_list[j])

            # append data to current weather
            current_weathers_dic['avg_coord'].append(average_coordinate)#
            current_weathers_dic['x_y_grid_pt'].append(x_y)
            current_weathers_dic['city_state'].append(city_name[i])
            current_weathers_dic['current_temp'].append(current_weather)
            current_weathers_dic['wind'].append(wind_speed)
            current_weathers_dic['description'].append(description)

            # shows coder what city number we are on in terminal
            print("City Number: ", i)
            
        # fixes the error where not every city has a forecast
        except KeyError as ke: 
            print(f"{ke}; {city_name[i]}")
            time.sleep(1)
            continue
        break


print(weather_forecast_dic)
# create dataframe then convert dictionary to .csv file
current_weather_DF = pd.DataFrame(current_weathers_dic)
current_weather_DF.to_csv("data/weather.csv", index=False)

weather_forecast_DF = pd.DataFrame(weather_forecast_dic)
weather_forecast_DF.to_csv("data/weather_forecast.csv", index=False)
print(current_weather_DF.head())
print(weather_forecast_DF.head())
# https://api.weather.gov/gridpoints/OKX/35,34/forecast

    