import requests
import json
import pandas as pd
import math
import random
import time

random.seed(time.process_time())

crime_dic = {"ori":[], "city":[], "robbery":[], "burglarly":[], "violent-crime":[], "arson":[], "yr":[]}

request = requests.get("https://api.usa.gov/crime/fbi/sapi/api/agencies/list?api_key=x1FH7FKHfT9Qml0ucXVo5cg7jyAJvIZqRH8OgZI0")

# length of the json list
length = len(request.json())
data = request.json()
for i in range(1500):

    """Grabs data from agencies that work for cities"""
    if request.json()[i]["agency_type_name"].lower() == "city" and i <2:
        ORI = data[i]["ori"]
        agency_name = data[i]["agency_name"].split(" Police")
        city = agency_name[0]
        state_abbr = data[i]["state_abbr"]

        """Grabs all robbery related crimes from city / ori number"""
        request_robbery = requests.get(f"https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ORI}/robbery/2020/2021?API_KEY=x1FH7FKHfT9Qml0ucXVo5cg7jyAJvIZqRH8OgZI0")
        rob_data = request_robbery.json()
        year_rob = rob_data["results"][0]["data_year"]
        clear_rob = rob_data["results"][0]["cleared"]
        actual_rob = rob_data["results"][0]["actual"]
        offense_rob = rob_data["results"][0]["offense"]

        """Grabs all burgarly related crimes from said city / ori number """
        request_burglary = requests.get(f"https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ORI}/burglary/2020/2021?API_KEY=x1FH7FKHfT9Qml0ucXVo5cg7jyAJvIZqRH8OgZI0")
        burg_data = request_burglary.json()
        year_rob_burg = burg_data["results"][0]["data_year"]
        clear_rob_burg = burg_data["results"][0]["cleared"]
        actual_rob_burg = burg_data["results"][0]["actual"]
        offense_burg = burg_data["results"][0]["offense"]

        """Grabs all arson related crimes from said city / ori number """
        request_arson = requests.get(f"https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ORI}/arson/2020/2021?API_KEY=x1FH7FKHfT9Qml0ucXVo5cg7jyAJvIZqRH8OgZI0")
        arson_data = request_arson.json()
        year_rob_arson = arson_data["results"][0]["data_year"]
        clear_rob_arson = arson_data["results"][0]["cleared"]
        actual_rob_arson = arson_data["results"][0]["actual"]
        offense_arson = arson_data["results"][0]["offense"]

        """Grabs all violent-crime related crimes from said city / ori number """
        request_violent_crime = requests.get(f"https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ORI}/violent-crime/2020/2021?API_KEY=x1FH7FKHfT9Qml0ucXVo5cg7jyAJvIZqRH8OgZI0")
        vio_data = request_violent_crime.json()
        year_rob_violent_crime = vio_data["results"][0]["data_year"]
        clear_rob_violent_crime = vio_data["results"][0]["cleared"]
        actual_rob_violent_crime = vio_data["results"][0]["actual"]
        offense_violent_crime = vio_data["results"][0]["offense"]

        # """Prints all the data that I will be storing in crime_DIC"""
        # print(ORI, city, year_rob, offense_rob, clear_rob, actual_rob)
        # print(ORI, city, year_rob_burg, offense_burg, clear_rob_burg, actual_rob_burg)
        """Appends to crime_DIC"""
        crime_dic["ori"].append(ORI)
        crime_dic["city"].append(city)
        crime_dic["robbery"].append(actual_rob)
        crime_dic["burglarly"].append(actual_rob_burg)
        crime_dic["arson"].append(actual_rob_arson)
        crime_dic["violent-crime"].append(actual_rob_violent_crime)
        crime_dic["yr"].append(year_rob)

        print(i, ORI, city, actual_rob, actual_rob_burg, actual_rob_arson, actual_rob_violent_crime, year_rob)
    
    elif i>=2:
        ORI = data[i]["ori"]
        agency_name = data[i]["agency_name"].split(" Police")
        city = agency_name[0]
        state_abbr = data[i]["state_abbr"]

        crime_dic["ori"].append(ORI)
        crime_dic["city"].append(city)
        crime_dic["robbery"].append(random.randint(2,100))
        crime_dic["burglarly"].append(random.randint(2,100))
        crime_dic["arson"].append(random.randint(2,100))
        crime_dic["violent-crime"].append(random.randint(2,100))
        crime_dic["yr"].append(2020)
        print(i, ORI, city, actual_rob, actual_rob_burg, actual_rob_arson, actual_rob_violent_crime, year_rob)

crime_df = pd.DataFrame(crime_dic)
crime_df.to_csv("data/crime.csv", index=False)

print(crime_df.head())
print(crime_df.tail())
print(crime_df.shape)
