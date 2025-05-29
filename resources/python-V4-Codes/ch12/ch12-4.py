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
queryTable = """create table Authors(
authorId varchar(20) primary key not Null,
aName    varchar(20) not NULL,
aFamily  varchar(20) not NULL,
degree   varchar(20),
email    varchar(20))"""
cursor.execute(queryTable)

if not cursor:
     print("Table not created...")
else:
    print("Table Authors created...")

