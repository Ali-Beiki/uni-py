x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
print("The result is : ", end = " ")
print((lambda x, y: x ** 2 + y ** 2)(x, y))
result = lambda x, y: x ** 2 + y ** 2
print("The result is : ", end = " ")
print(result(x, y))
