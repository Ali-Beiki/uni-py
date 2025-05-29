import sqlite3 as db
from prettytable import PrettyTable
myConnection = db.connect('University.db')
cursor = myConnection.cursor()
if not cursor:
    print("An Error ocuured")
    quit()
query =  "create table Students( "
query += "stNo integer primary key, "
query += "Name text, "
query += "Average real)"
cursor.execute(query)
inquery = query = """insert into Students
(stNo, Name, Average) values(?, ?, ?)"""
num = 3
records = []
for i in range (0, num):
    id = int(input("Enter st number : "))
    iname = input("Enter name : ")
    ave = float(input("Enter average : "))
    rec = (id, iname, ave)
    records.append(rec)
cursor.executemany(query, records)
myConnection.commit()
print(cursor.rowcount, " records inserted.")
selQuery = "select * from Students"
cursor.execute(selQuery)
result = cursor.fetchall()
table = PrettyTable(['St number', 'Name', 'Average'])
for rec in result:
    table.add_row(rec)  
print(table)



