-- Brandon
CREATE TABLE General (
    city VARCHAR(20) NOT NULL,
    county VARCHAR(20) NOT NULL,
    state_id CHAR(2) NOT NULL,
    populations INTEGER(10) NOT NULL,
    pop_density INTEGER(6) NOT NULL,
    time_zone VARCHAR(20) NOT NULL,
    zip_codes VARCHAR(1000)
);

-- Brandon
CREATE TABLE AQI (
    city VARCHAR(20) NOT NULL,
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
);

-- Brandon
CREATE TABLE AQI_Forecast(
    city VARCHAR(20) NOT NULL,
    time_updated datetime,
    AQI INTEGER(3) NOT NULL,
    PM10 INTEGER(4),
    PM25 INTEGER(4)
);
 
-- Isaac
CREATE TABLE Weather(
    city VARCHAR(20) NOT NULL
);

-- Isaac
CREATE TABLE Radiation(
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL,
    avg_dni DECIMAL(6, 4),
    avg_ghi DECIMAL(6, 4)
);

-- Brandon
CREATE TABLE Water_Quality(
    levels INTEGER(10) NOT NULL
);

-- Isaac
CREATE TABLE Crime_Rates(
    cancer INTEGER(10) NOT NULL
);