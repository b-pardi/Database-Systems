CREATE TABLE General (
    city VARCHAR(20) NOT NULL,
    county VARCHAR(20) NOT NULL,
    state_id CHAR(2) NOT NULL,
    populations INTEGER(10) NOT NULL,
    pop_density INTEGER(6) NOT NULL,
    time_zone VARCHAR(20) NOT NULL,
    zip_codes VARCHAR(1000)
);

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

CREATE TABLE AQI_Forecast(
    city VARCHAR(20) NOT NULL,
    time_updated datetime,
    AQI INTEGER(3) NOT NULL,
    PM10 INTEGER(4),
    PM25 INTEGER(4)
);
 
CREATE TABLE Weather(
    city VARCHAR(20) NOT NULL
);

CREATE TABLE Radiation(
    levels INTEGER(10) NOT NULL
);

CREATE TABLE Toxicology(
    levels INTEGER(10) NOT NULL
);

CREATE TABLE Disease_Rates(
    cancer INTEGER(10) NOT NULL
);