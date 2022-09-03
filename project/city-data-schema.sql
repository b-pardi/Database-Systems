CREATE TABLE AQI(
    City VARCHAR(20) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL,
    Time_updated datetime,
    AQI INTEGER(3) NOT NULL,
    CO INTEGER(4),
    H INTEGER(4),
    NO2 INTEGER(4),
    Ozone INTEGER(4),
    PM10 INTEGER(4),
    PM25 INTEGER(4)
)

CREATE TABLE AQI_Forecast(
    City VARCHAR(20) NOT NULL,
    Time_updated datetime,
    AQI INTEGER(3) NOT NULL,
    PM10 INTEGER(4),
    PM25 INTEGER(4)
)
 
CREATE TABLE Weather(
    City VARCHAR(20) NOT NULL
)