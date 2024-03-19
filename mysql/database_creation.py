# create tables


try:
    connection = mysql.connector.connect(
        host="localhost", database="Thanks_Alatte", user="root", password="password"
    )
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
