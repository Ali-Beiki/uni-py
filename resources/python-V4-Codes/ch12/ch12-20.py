import mysql.connector as mysql
import os
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
      select title, bookSubject
      from Books, BookSubjects
      where
      Books.subjectId = BookSubjects.subjectId
     """
cursor.execute(query)
os.system('cls')
result = cursor.fetchall()
for rec in result: 
    print("title = ", rec[0], )
    print("bookSubject  = ", rec[1], "\n")
   
