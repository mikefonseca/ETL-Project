
-- Create the database
CREATE DATABASE car;

-- establish a connection to the created database
\c car;

-- create a table for the ratings
CREATE TABLE ratings(
year int,
mfg char(50),
model char(50),
rating numeric);

-- check out the column datatypes set up 
select column_name, data_type from information_schema.columns
where table_name = 'ratings';

-- read in the file from a directory with privileges into the ratings table
COPY ratings FROM 'C:\tmp\Ratings_2008_cleaned.csv' DELIMITER ',' CSV HEADER;


-- create a table for the 
CREATE TABLE vehicles (
idx int PRIMARY KEY,
year int,
mfg char(50),
model varchar(250),
condition char(50),
mileage numeric,
status char(50),
type char(50));

-- check out the column types
select column_name, data_type from information_schema.columns
where table_name = 'vehicles';

-- populate table 
SET CLIENT_ENCODING TO 'utf8';
COPY vehicles FROM 'C:\tmp\Used_Vehicles_cleaned.csv' DELIMITER ','  CSV HEADER  NULL AS 'NULL' ;


--perform merge of two tables based on conditions 
WITH t AS (SELECT * FROM vehicles WHERE condition = 'excellent' AND status = 'clean')
SELECT *
FROM t	
JOIN ratings
	ON t.mfg = ratings.mfg
	AND t.year = ratings.year
	AND t.model = ratings.model
;