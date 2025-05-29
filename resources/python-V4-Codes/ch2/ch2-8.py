x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0
sign = 1
for i in range(1, n + 1, 2):
    sum = sum + (x ** i) * sign
    sign = -sign
print("Sum = ", sum)
