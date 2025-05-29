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
queryTable = """insert into BookSubjects
(subjectId, bookSubject)
values
('01', 'Programming'),  
('02', 'Softwarw'), 
('03', 'Computer Networks'), 
('04', 'Information Technology'), 
('05','Cloud Computing') """
cursor.execute(queryTable)
myConnection.commit()
