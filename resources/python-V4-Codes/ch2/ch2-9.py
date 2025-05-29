oddSum = 0
evenSum = 0
for i in range(1, 100, 2):
    oddSum += i
for j in range(2, 101, 2):
    evenSum += j
print("sum of even numbers = ", evenSum)
print("Sum of odd numbers = ", oddSum)
