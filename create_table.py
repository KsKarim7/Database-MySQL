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
    CREATE TABLE Student
    (
        Roll varchar(4),
        Name varchar(50)
    )
"""

mycursor.execute(SQLquery)
print("Created table successfully")