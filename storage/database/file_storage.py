#!/usr/bin/python3

import mysql.connector

class DatabaseManager():
    def __init__(self):
        #Establishing Connection with the mysqlDB
        self.connection = mysql.connector.connect (
                host='localhost',
                user='root',
                password='root@2024',
                database='LibrarySystem'
                )

        # Cursor object to execute SQL queries
        self.cursor = connection.cursor()
    
    def insert_guest_requests(self):
        #SQL query
        query = "INSERT INTO user_information(first_name, last_name, date_of_birth, password, username) VALUES(%s, %s, %s, %s, %s)"

        # Execute the query with the given data
        self.cursor.execute(query, (first_name, last_name, date_of_birth, password, username))
        
        # Commit the Changes
        self.connection.commit()

    def close_connection(self):
        cursor.close()
        connection.close()
