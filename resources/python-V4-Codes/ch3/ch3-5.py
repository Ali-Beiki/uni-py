def swap(a, b):
    a, b = b, a
    return a, b
#------------------
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x, y = swap(x, y)
print("After swap: x = ", x, ", y = ", y)
