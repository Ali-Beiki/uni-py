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
queryTable = "select * from Books"
cursor.execute(queryTable)
list = cursor.fetchall()
for rec in list:
    print(rec)
