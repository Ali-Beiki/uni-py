done = True
odds = 0
while done:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("The number is even, enter odd number!")
        continue
    odds += num
    ans = input("Do you want to continue (y/n)? ")
    if ans == "y" or ans == "Y":
        continue
    done = False
print("Sum of odd numbers is: ", odds)
