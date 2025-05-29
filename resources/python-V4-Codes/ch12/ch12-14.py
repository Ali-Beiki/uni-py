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
query = """insert into City
(cityCode, cityName) values(%s, %s)"""
#Enter the number of records
n = int(input("Enter number of records : "))
records = []
for i in range (0, n):
    print("Enter record number " + str(i + 1)+ " : ")
    ccode = input("Enter city code: ")
    cname = input("Enter city name: ")
    rec = (ccode, cname)
    records.append(rec)
print(records)
cursor.executemany(query, records)
myConnection.commit()
print(cursor.rowcount, " records inserted.")

          
    
