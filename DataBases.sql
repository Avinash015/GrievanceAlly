-- create  different database for all ministry and one database is combine

-- water minisrey 
CREATE DATABASE water_ministry_db;
USE water_ministry_db; -- Switch to the database where you want to create the table

CREATE TABLE ministry_complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_description TEXT,
    token_id VARCHAR(10),
    pincode varchar(6),
    adhar_number varchar(12)
    
);

-- elecrticity ministry
CREATE DATABASE electricity_ministry_db;
USE electricity_ministry_db; -- Switch to the database where you want to create the table

CREATE TABLE ministry_complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_description TEXT,
    token_id VARCHAR(10),
    pincode varchar(6),
    adhar_number varchar(12)
);


-- road ministry
CREATE DATABASE roads_ministry_db;
USE roads_ministry_db; -- Switch to the database where you want to create the table

CREATE TABLE ministry_complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_description TEXT,
    token_id VARCHAR(10),
    pincode varchar(6),
    adhar_number varchar(12)
);


-- all ministry
CREATE DATABASE all_ministries_db;
USE all_ministries_db; -- Switch to the database where you want to create the table

CREATE TABLE all_complaints  (
    id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_description TEXT,
    ministry varchar(255),
    token_id VARCHAR(10),
    pincode varchar(6),
    adhar_number varchar(12)
);
-- if you show data  for all ministry

-- for water
USE water_ministry_db;


select * from ministry_complaints;

-- for electricity
USE electricity_ministry_db; 
select * from ministry_complaints;

-- for road
USE roads_ministry_db;
select * from ministry_complaints
;

-- for all ministry
USE all_ministries_db;
select * from all_complaints;

-- don't run this query
drop table all_complaints;