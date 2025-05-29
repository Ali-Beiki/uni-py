import mysql.connector as mysql
import os
import tabulate
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
query = """
      select title, price, aName, aFamily 
      from Books, Authors
      where
      Books.authorId = Authors.authorId
     """
cursor.execute(query)
os.system('cls')
result = cursor.fetchall()
table = PrettyTable(['Title', 'Price',
                     'Authon Name', 'Author Family'])
for rec in result:
    table.add_row(rec)
    
print(table)




