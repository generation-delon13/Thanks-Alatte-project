# import mysql.connector

import mysql.connector
from mysql.connector import Error

# connecting to my mysql
try:
    connection = mysql.connector.connect(
        host="localhost", database="Thanks_Alatte", user="root", password="password"
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
print("Welcome to Thanks Alatte cafe")
