.mode csv
.separator ','
.headers off
.import data/uscities_scrubbed.csv Cities_General
.import data/aqi.csv AQI
.import data/forecasted_aqi.csv AQI_Forecast
.import data/org_water_updated.csv Water_Quality