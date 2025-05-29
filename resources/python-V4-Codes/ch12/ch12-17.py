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
query = """select title, price, aName, aFamily
           from Books, Authors
           where Books.authorId = Authors.authorId
        """
cursor.execute(query)
result = cursor.fetchall()
for rec in result:
    print(rec)
