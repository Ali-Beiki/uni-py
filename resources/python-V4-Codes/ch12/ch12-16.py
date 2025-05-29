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
query = """select title, price , pageNo
        from books
        where price between 600 and 15000
        order by price desc
       """
cursor.execute(query)
result = cursor.fetchall()
for rec in result:
    print(rec)
