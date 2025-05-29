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
queryTable = """create table City(
cityCode varchar(10) primary key not Null,
cityName   varchar(20) not NULL)"""
cursor.execute(queryTable)

if not cursor:
     print("Table not created...")
else:
    print("Table City created...")
cursor.execute("show tables")
for table in cursor:
    print(table)
