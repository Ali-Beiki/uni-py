numbers = []
while len(numbers) < 20:
    num = int(input(f"Enter number {len(numbers)+1} (10-100): "))
    if 10 <= num <= 100 and num not in numbers:
        numbers.append(num)
    else:
        print("Invalid or duplicate number!")

print("Unique numbers:", numbers)