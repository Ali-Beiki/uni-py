odds = 0
evens = 0
while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break
    if num % 2 == 0:
        evens += num
    else:
        odds += num
print("Sum of odds = ", odds, " sum of evens = ", evens)
