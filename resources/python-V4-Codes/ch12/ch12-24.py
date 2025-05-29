import mysql.connector as mysql
from prettytable import PrettyTable
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
query = "delete from Sbooks"
cursor.execute(query)
cursor.execute("select * from Sbooks")
result = cursor.fetchall()
table = PrettyTable(['ISBN', 'Title', 'Price'])
for rec in result:
    table.add_row(rec)  
print(table)
