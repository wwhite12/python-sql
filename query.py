import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bamazon',
                                         user='root',
                                         password='XXXX')
    #now connected, go into query
    sqlQuery = "SELECT * FROM Products"
    cursor = connection.cursor()
    cursor.execute(sqlQuery)
    records = cursor.fetchall()
    print("Total rows in table",cursor.rowcount)

    for row in records:
        print("ID = ", row[0])
        print("Product name = ",row[1])
        print("dep_name = ",row[2])
        print("price = ",row[3])
        print("stock = ",row[4])
        

except Error as e:
    print("Error reading MySQL table",e)

finally: 
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")