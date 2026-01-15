-- Database: weather

-- DROP DATABASE IF EXISTS weather;

CREATE DATABASE weather
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;



	CREATE TABLE weather_data (
    time TIMESTAMP,
    date DATE,
    hour INT,
    temperature FLOAT
);

select * from weather_data;