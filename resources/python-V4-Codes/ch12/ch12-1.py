import mysql.connector as mysql

myConnection = mysql.connect(
    host = "localhost",
    user = "root",
    password = "Ghomi@2020"
)

cursor = myConnection.cursor()
if cursor:
    print("Connection is OK")
else:
    print("An Error ocuured")
myConnection.close()
