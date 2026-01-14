CREATE TABLE sam (
  area_sqft   INTEGER,
  bedrooms    INTEGER,
  bathrooms   INTEGER,
  stories     INTEGER,
  parking     INTEGER,
  age_years   INTEGER,
  city        TEXT,
  near_school TEXT,     -- Yes/No
  price       INTEGER
);
select * from sam;

select near_school,count(*) from sam group by near_school; 


SELECT * FROM sam LIMIT 5;

select city,count(*) from sam group by city;
