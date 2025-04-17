import numpy as np

numbers =[]

number = int(input(f'Enter Number {len(numbers)+1} :'))

while number != 0 :
    numbers.append(number)
    number = int(input(f'Enter Number {len(numbers)+1} :'))

unique, counts = np.unique(numbers, return_counts=True) # مقدار تکرار هر ایتم در ارایه

print("unique :",unique)
print("counts :",counts)

most_frequent = unique[np.argmax(counts)]



print("numbers :",numbers)
print("most_frequent :",most_frequent)