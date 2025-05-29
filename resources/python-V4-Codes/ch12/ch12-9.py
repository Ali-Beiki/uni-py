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
queryTable = """alter table Books
drop newColumn """
cursor.execute(queryTable)
cursor.execute("describe Books")
indexList = cursor.fetchall();
for s in indexList:
    print(s)
