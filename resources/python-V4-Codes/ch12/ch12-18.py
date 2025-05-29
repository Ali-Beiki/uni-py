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
start = int(input("Enter start record : "))
num = int(input("Enter number of records : "))
          
q1 =   "select title, price, pageNo"  
q2 =    q1 + " from Books limit " + str(num)  
query =  q2 + " offset " + str(start)  
cursor.execute(query)
result = cursor.fetchall()
for rec in result:
    print(rec)
