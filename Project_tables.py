import mysql.connector
from mysql.connector import Error
# connecting to my mysql
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Thanks_Alatte',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
print('Welcome to Thanks Alatte cafe')


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Thanks_Alatte',
                                         user='root',
                                         password='password')
    mySql_Create_Table_Query = """CREATE TABLE Transcations (
                             Date varchar(250) NOT NULL,
                             Time varchar(250) NOT NULL,
                             Location varchar(250) NOT NULL,
                             Transaction_ID int(11) NOT NULL AUTO_INCREMENT,
                             Products_Purchased varchar(250) NOT NULL,
                             Total_Price float NOT NULL,
                             Payment_Method varchar(250) NOT NULL,
                             PRIMARY KEY (Transaction_ID)) """
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Transcations Table created successfully ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))




    
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Thanks_Alatte',
                                         user='root',
                                         password='password')
    mySql_Create_Table_Query = """CREATE TABLE Orders (
                             Order_ID int(11) NOT NULL AUTO_INCREMENT,
                             Transaction_ID int(11) NOT NULL,
                             Product_ID int(11) NOT NULL,
                             Product_Purchased varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Payment_Method varchar(250) NOT NULL,
                             PRIMARY KEY (Order_ID)) """
                             
                             
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Orders Table created successfully ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))    
    
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Thanks_Alatte',
                                         user='root',
                                         password='password')
    mySql_Create_Table_Query = """CREATE TABLE Products (
                             Product_ID int(11) NOT NULL AUTO_INCREMENT,
                             Product varchar(250) NOT NULL,
                             Price float NOT NULL,
                             PRIMARY KEY (Product_ID)) """
                             
                             
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Products Table created successfully ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))        