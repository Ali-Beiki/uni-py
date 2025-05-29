## Driver program to test the class
from rectangleModule import rectangle
width, length = input("Enter width and length of rectangle: ").split()
rec = rectangle(int(width), int(length))
print(rec)
print(rec.width)        
