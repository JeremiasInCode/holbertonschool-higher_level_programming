-- Creates the database hbtn_0d_usa and the table states
DROP DATABASE IF EXISTS hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE auto_increment not null PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);