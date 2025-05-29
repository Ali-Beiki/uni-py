import mysql.connector as mysql
myConnection = mysql.connect(
    host = "localhost",
    user = "root",
    password = "Ghomi@2020",
    database = "Publications"
)
cursor = myConnection.cursor()
if not cursor:
    print("An Error ocuured")
    quit()
pName = input("Enter publisher name : ")
query = "select pubName, telNo, webURL "
query += " from Publishers where pubName = '"
query += pName + "'"
cursor.execute(query)
result = cursor.fetchall()
if cursor.rowcount != 0:
    print("Record found :")  
    for rec in result:
      print(rec)
else:   
    print("Record not found! ")
