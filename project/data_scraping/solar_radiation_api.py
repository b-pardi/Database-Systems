import requests
import json
import pandas as pd


solar_DIC = {"avg_coord":[], "avg_dni":[], "avg_ghi":[], "avg_lat_tilt":[]}
weather_df = pd.read_csv("data/weather.csv")
cities_df = pd.read_csv("data/uscities_scrubbed.csv")
latitude = cities_df['lat']
longitude = cities_df['lng']
city_name = cities_df['city_state']

length = len(weather_df)

print(length)
for i in range(length):

    if i < 50:
        request = requests.get(f"https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=la2e7VCjlZowvrSdEF0VNp0ETF6qiOtQJg3BkwH0&lat={latitude[i]}&lon={longitude[i]}")
        avg_dni = request.json()["outputs"]["avg_dni"]["annual"]
        avg_ghi = request.json()["outputs"]["avg_ghi"]["annual"]
        avg_lat_tilt = request.json()["outputs"]["avg_lat_tilt"]["annual"]

        average_coordinate  = (latitude[i] + longitude[i]) / 2
        solar_DIC["avg_coord"].append(average_coordinate)
        solar_DIC["avg_dni"].append(avg_dni)
        solar_DIC["avg_ghi"].append(avg_ghi)
        solar_DIC["avg_lat_tilt"].append(avg_lat_tilt)
        print(f"{city_name[i]}, {average_coordinate}")
    elif i >=50:
        average_coordinate  = (latitude[i] + longitude[i]) / 2
        solar_DIC["avg_coord"].append(average_coordinate)
        solar_DIC["avg_dni"].append("NaN")
        solar_DIC["avg_ghi"].append("NaN")
        solar_DIC["avg_lat_tilt"].append("NaN")

    


solar_df = pd.DataFrame(solar_DIC)
solar_df['avg_coord'] = solar_df['avg_coord'].astype('float')
print(weather_df.shape)
print(solar_df.shape)
weather_df = pd.merge(weather_df, solar_df, on = "avg_coord")
print(weather_df.head())
print(weather_df.tail())
print(weather_df.shape)
weather_df.to_csv("data/weather_and_solar.csv", index=False)
# code works 
