def getTemp(temp):
   for i in range(len(temp)):
      temp [i] = [int(x) for x in input("Enter five values: ").split()]
#----------------------------------------------------
def display(temp):
    print("Contents of list: ")
    for i in range(len(temp)):
        for j in range(len(temp[0])):
             print("{0:4d}".format(temp[i][j]), end = " ")
        print()
    print("-------------------------")
#--------------------------------------------------
def findMean(temp):
    days = ["wed", "Thur", "Friday"]
    print("{0:7s} {1:7s}".format("Days", "Averages"))
    print("-------------------------") 
    for i in range(len(temp)):
        daySum = 0
        for j in range (len(temp[0])):
             daySum += temp[i][j]
        print("{0:7s} {1:8.2f}".format(days[i], daySum /len(temp[0])))
## Driver program to test #########        
rows = 3
cols = 5
temp = [ ([0] * cols) for row in range(rows) ]
getTemp(temp)
display(temp)
findMean(temp)
