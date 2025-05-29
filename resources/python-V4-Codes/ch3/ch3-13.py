def mixed(stno, yaer, *grades, **courses):
    print("stno = ", stno)
    print("year = ", yaer)
    print("grades = ", grades)
    print("courses = ", courses)
#------------------------------------
mixed(100, 98 , 12, 14, 19 ,
      course1  = "Math", course2 = "Prog", course3 = "Data" )
