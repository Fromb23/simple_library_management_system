CREATE DATABASE LibrarySystem;

CREATE TABLE user_information (
	user_id VARCHAR(20) PRIMARY KEY,
	first_name VARCHAR(10),
	last_name VARCHAR(10),
	username VARCHAR(10) DEFAULT NULL,
	email VARCHAR(30) DEFAULT NULL,
	date_of_birth VARCHAR(10) DEFAULT NULL,
	password VARCHAR(10) DEFAULT NULL
);

INSERT INTO user_information(user_id, first_name, last_name, username, email, date_of_birth, password)
VALUES (%s, %s, %s, %s, %s, %s, %s)
