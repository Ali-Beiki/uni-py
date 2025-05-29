import mysql.connector as mysql

myConnection = mysql.connect(
    host = "localhost",
    user = "root",
    password = "Ghomi@2020"
)
cursor = myConnection.cursor()
if cursor:
    cursor.execute("create database Publications")
    print("Databse Publications is created")
    
else:
    print("An Error ocuured")

cursor.execute("show databases")
databases = cursor.fetchall()
print("------------------------\n")
for database in databases:
    print(database)

