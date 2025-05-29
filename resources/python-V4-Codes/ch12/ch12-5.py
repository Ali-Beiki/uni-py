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
queryTable = """create table Publishers(
pubId varchar(10) primary key not Null,
pubName    varchar(20) not NULL,
telNo          varchar(15),
webURL         varchar(30),
cityCode       varchar(10),
mName          varchar(20),
mLname         varchar(20))"""
cursor.execute(queryTable)

if not cursor:
     print("Table not created...")
else:
    print("Table Publishers created...")

