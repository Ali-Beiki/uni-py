## Driver program ##########
from searchModule import * 
import numpy as np
arr = np.array([0] * 5)
for i in range(len(arr)):
    arr[i] = int(input("Enter student number : "))
item = int(input("Enter a number to search: "))
result = seqSearch(arr, item)
print("Result of sequential search :")
if result >= 0:
    print("Value ", item, " exist at position ", result)
else:
    print("Value ", item, " not exist")
   
bubble(arr)
print("Array after sorting: ")
print(arr)
print("Result of binary search :") 
result = binSearch(arr, item)
if result >= 0:
    print("Value ", item, " exist at position ", result)
else:
    print("Value ", item, " not exist")
    
                 

            
        
