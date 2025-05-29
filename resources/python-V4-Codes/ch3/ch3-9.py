def maxFind(*par):
    myMax = par[0]
    for item in par[1:]:
        if item > myMax:
            myMax = item
    return myMax
#------------------------
max1 = maxFind(5,13, 4, 18, 7)
print("In firs call, max is : ", max1)
max2 = maxFind(7, 9, 4)
print("In second call, max is : ", max2)
