import mysql.connector as mysql
from prettytable import PrettyTable
myConnection = mysql.connect(
    host = "localhost",
    user = "root",
    password = "Ghomi@2020",
    database = "Publications"
)
cursor = myConnection.cursor()
cursor.execute("drop table Sbooks")
if not cursor:
    print("An Error ocuured")
    quit()
queryTable = """create table Sbooks(
ISBN varchar(20) primary key not null,
title varchar(30) not null,
price int)"""
cursor.execute(queryTable)

if not cursor:
     print("Table not created...")
else:
    print("Table Sbooks created...")
cursor.execute("show tables")
for table in cursor:
    print(table)
selQuery = """insert into Sbooks(isbn, title, price)
              select isbn, title, price from Books"""
cursor.execute(selQuery)
myConnection.commit()
cursor.execute("select * from Sbooks")

result = cursor.fetchall()
table = PrettyTable(['ISBN', 'Title', 'Price'])
for rec in result:
    table.add_row(rec)
    
print(table)
