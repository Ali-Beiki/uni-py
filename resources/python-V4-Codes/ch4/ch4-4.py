import numpy as np
def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#----------------------------------------
temp = np.array([' '] * 5, dtype = 'object')
for i in range(len(temp)):
    temp[i] = input("Enter a word: ")
print("Before sorting: ")
print(temp)
bubble(temp)
print("After sorting: ")
print(temp)
