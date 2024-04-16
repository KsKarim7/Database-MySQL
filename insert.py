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
    INSERT INTO Student(Roll,Name) 
    VALUES('1091','Mohammad Khalz')
"""

mycursor.execute(SQLquery)
mydbconnection.commit()
print("Inserted table successfully")