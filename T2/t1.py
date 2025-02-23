countNumber =int(input("Enter Count Number :"))

total =0
for i in range(countNumber):
    number =int(input(f"Enter {i+1} Number : "))
    total += number **3


print(f"total cube Number :{total}")