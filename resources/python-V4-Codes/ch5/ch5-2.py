def getData(grList, nameList):
    name, ave  = input("Enter name and ave: ").split()
    grList.append(float(ave))
    nameList.append(name)
#--------------------------------------------
def delData(grList, nameList):
    name = input("Enter name to delete: ")
    if name in nameList:
        index = nameList.index(name)
        grList.pop(index)
        nameList.pop(index)
    else:
        print("The name ", name , " not found")
        input("Press a key to continue: ")
#---------------------------------------------
def display(grList, nameList):
    print("{0:7s} {1:7s}".format("Name", "Average"))
    for i in range(len(nameList)):
        print("{0:7s} {1:8.2f}".format(nameList[i], grList[i]))
#-------------------------------------------------
def iteration(grlist):
    ave = float(input("Enter an ave to count :"))
    print("The counts of ", ave, " is ", grList.count(ave))
#---------------------------------------------------
def menu():
    print("1. Enter data")
    print("2. Remove data")
    print("3. Find iterations:")
    print("4. Display data")
    print("5. Exit")
    choice = int(input("Enter your select(1-5): "))
    return choice
#-------------------------------------------------------
grList = []
nameList = []
while True:
    c = menu() 
    if c == 1:
        getData(grList, nameList)
    elif c == 2:
        delData(grList, nameList)
    elif c == 3:
        iteration(grList)
    elif c == 4:
        display(grList, nameList)
    else:
        break
#--------------------------------------
        
        
