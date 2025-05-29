op = input("Enter an operater : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if op == "+" :
    result = num1 + num2
    print("num1 + num2 = ", result)
elif op == "-" :
    result = num1 - num2
    print("num1 - num2 = ", result)
elif op == "**" :
    result = num1 ** num2
    print("num1 ** num2 = ", result)
elif op == "/" :
    result = num1 / num2
    print("num1 / num2 = ", result)
elif op == "*" :
    result = num1 * num2
    print("num1 * num2 = ", result)
elif op == "//" :
    result = num1 // num2
    print("num1 // num2 = ", result)
else :
    print("operator is illegal.")
