import mysql.connector

db_name = "python_test_db"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "password",
    database = db_name
)


mycursor = mydbconnection.cursor()

SQLquery = """
    UPDATE Student 
    SET Name = 'Khalidzza'
    WHERE Name = 'Mohammad Khalz'
"""

mycursor.execute(SQLquery)
mydbconnection.commit()

print("Updated table successfully")