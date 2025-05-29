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
query = "select title, price, bookSubject "
query += "from Books as b, BookSubjects as bs "
query += "where b.subjectId = bs.subjectId"
cursor.execute(query)
result = cursor.fetchall()
table = PrettyTable(['Title', 'Price', 'Subject'])
for rec in result:
    table.add_row(rec)  
print(table)
