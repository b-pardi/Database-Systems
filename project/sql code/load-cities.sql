.mode csv
.separator ','
.headers off
.import data/uscities_scrubbed.csv Cities_General
.import data/aqi.csv AQI
.import data/forecasted_aqi.csv AQI_Forecast
.import data/org_water_updated.csv Water_Quality
.import data/weather_and_solar.csv Current_Weather
.import data/weather_forecast.csv Forecasted_Weather
.import data/crime.csv Crime_Rates
.import data/states.csv states_key
.import data/cities_water_bridge.csv cities_water_relation