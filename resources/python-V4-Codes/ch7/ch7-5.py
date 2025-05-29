## Driver program to test
from studentListModule import studentList
def menu():
    print()
    print("1. Enter a student ")
    print("2. Find best student ")
    print("3. Delete a student ")
    print("4. Search a student ")
    print("5. Report list ")
    print("6. Exit ")
    choice = int(input("\nEnter your select(1 - 6) : "))
    return choice
## end of menu function
def addtoList(stlist):
    name, stno, ave = input("Enter name, stno, ave: ").split()
    st = studentList(name, int(stno), float(ave))
    stlist.append(st)
def findMax(stlist):
    mAve = stlist[0].getAve() # mAve = first ave
    p = 0 # p is the position of maximum element
    for i in range(1, len(stlist)):
       if stlist[i].getAve() > mAve :
           mAve = stlist[i].getAve()
           p = i
    print("Student with maximum ave :")
    print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
    stlist[p].display()
##-------------------------------------------
def searchStudent(stlist) :
    stno = int(input("Enter stno to search : "))
    found = False # student not found
    i = 0 #index of list
    while i < len(stlist) and not found :
       if stlist[i].getStno() == stno :
            found = True
       else:
            i = i + 1 
    if not found :
        print("Student with ", stno ," not exist.")
    else :
        print("Student with ", stno , " exist.")
        print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
        stlist[i].display()
## end of searchStudent()
def delStudent(stlist) :
    stno = int(input("Enter stno to delete : "))
    found = False # student not found
    i = 1  #index of list
    while  i < len(stlist) and not found :
       if stlist[i].getStno() == stno :
           found = True
       else:
           i = i + 1
    if not found :
        print("Student with ", stno ," not exist.")
    else :
        stlist.pop(i) # delete student
        print("Student with ", stno , " deleted.")
## end of delStudent()
def reportList(stlist) :
    print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
    for  i in range(len(stlist)) :
        stlist[i].display()
## end of while
## end of report()        
##-------------------------------------------
stlist = list()
while True:
    c = menu()
    if c == 1:
        addtoList(stlist)
    elif c == 2:
        findMax(stlist)
    elif c == 3:
        delStudent(stlist)
    elif c == 4:
        searchStudent(stlist)
    elif c == 5:
        reportList(stlist)
    else:
        break
## end of while
