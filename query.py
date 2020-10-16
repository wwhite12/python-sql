import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bamazon',
                                         user='root',
                                         password='XXXXX')
    #now connected, go into query
    sqlQuery = "SELECT * FROM Products"
    cursor = connection.cursor()
    cursor.execute(sqlQuery)
    records = cursor.fetchall()
    print("Total rows in table",cursor.rowcount)

except Error as e:
    print("Error reading MySQL table",e)

finally: 
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")