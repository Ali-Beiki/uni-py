def compare(*numbers, case):
    if case:
        result = findMax(numbers)
    else:
        result = findMin(numbers)
    return result
#----------------------
def findMax(numbers):
    max = numbers[0]
    for item in numbers[:] :
        if item > max:
            max = item
    return max
#-----------------------
def findMin(numbers):
    min = numbers[0]
    for item in numbers[:] :
        if item < min:
            min = item
    return min
#----------------------
print("Max is : ", end = " ")
print(compare(5, 10, 6, case = True))
print("Min is : ", end = " ")
print(compare(5, 10, 6, case = False))       




