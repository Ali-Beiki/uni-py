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
queryTable = """insert into Authors
values
('01', 'Roger', 'Pressman', 'PHD', 'pressman@yahoo.com'),
('02', 'Einollah', 'Jafarnejad', 'PHD', 'jghomim@yahoo.com'),
('03', 'Javad', 'Vahidi', 'PHD', 'vahidi@yahoo.com'),
('04', 'Homayon', 'Motameni', 'PHD', 'motameni@yahoo.com'),
('05', 'Ghodrat', 'Sepidnam', 'PHD', 'sepidnam@yahoo.com'),
('06', 'Navid', 'Farrokhi', 'Master', 'farrokhi@yahoo.com')"""

cursor.execute(queryTable)
myConnection.commit()
