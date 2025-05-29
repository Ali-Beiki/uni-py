import numpy as np
def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#----------------------------------------
def seqSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1
#---------------------------------------
def binSearch(arr, item):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif item > arr[mid]: 
            low = mid + 1
        else:
            high = mid - 1
    return -1
        
