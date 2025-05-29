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
queryTable = """create table Books(
ISBN varchar(20) primary key not Null,
title varchar(30) not NULL,
pageNo int,
price int,
editNo int,
printNo int,
subjectId varchar(10),
pubId varchar(10),
authorId varchar(10))"""
cursor.execute(queryTable)

if not cursor:
     print("Table not created...")
else:
    print("Table Books created...")
