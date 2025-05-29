import numpy as np
grades = np.zeros(5)
for i in range(len(grades)):
    grades[i] = int(input("Enter a grade: "))
print("Array is: ")
print(grades)
min = np.amin(grades, 0)
max = np.amax(grades, 0)
print("Max = ", max, " , Min = ", min)
item = 20
x = np.where(grades == item)
if len(x[0]):
    print("Number ", item, " found at ", x[0])
else :
    print("Number ", item, " not found")
    
