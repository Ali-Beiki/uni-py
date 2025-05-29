import numpy as np
a = np.arange(9)
a = np.array([5, 10, 15, 18, 30, 40, 50, 60, 70])
print("First array: ")
print(a)
print("Split array to 3 section :")
b = np.split(a, 3)
print(b)
print("split using 1-d array :")
c = np.split(a, [2, 7])
print(c)

