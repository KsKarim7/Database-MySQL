import mysql.connector

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "password"
)
print(mydbconnection)

db_name = "python_test_db"
mycursor = mydbconnection.cursor()

SQLquery = "CREATE DATABASE " + db_name

mycursor.execute(SQLquery)