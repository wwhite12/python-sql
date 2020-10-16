import mysql.connector
from mysql.connector import Error

#Establish connection to MySQL server & DB

try:
    connection = mysql.connector.connect(host='localhost',
                                 database='bamazon',
                                 user='root',
                                 password='XXXXXX')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL server version ",db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Connected to database ",record)
except Error as e:
    print("Error while connecting to MySQL ",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")