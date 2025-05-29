def findMax(a, b, c):
    maxp = a if a > b else b
    maxp = c if c > maxp else maxp
    return maxp
#---------------------------------
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
maxNum = findMax(x, y, z)
print("The maximum number is : ", maxNum)
