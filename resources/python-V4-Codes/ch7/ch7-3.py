## Driver program to test
from circleModule import circle
rad = int(input("Enter the radius: "))
cir = circle()
cir.setRad(rad)
print("Radius is: {0:5d}".format(cir.getRad()))
print("Perimeter is : {0:8.2f}".format(cir.cirPerime()))
print("Area is : {0:8.2f}".format(cir.cirArea()))


