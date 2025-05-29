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
queryTable = """insert into Publishers
values
('501', 'olomrayaneh',  '32360772', 'olomrayaneh.net', '11', 'Einollah', 'jafarnejad'),
('502', 'daneshbonyan', '32314017', 'daneshbonyan.net', '11', 'Fatemeh', 'jafarnejad'),
('503', 'daneshnegar', '66416676', 'daneshnegar.net', '21', 'Reza', 'hatami'),
('504', 'elmohonar', '33416676', 'elmohonar.net', '31', 'Ali', 'ahmadi')"""

cursor.execute(queryTable)
myConnection.commit()
