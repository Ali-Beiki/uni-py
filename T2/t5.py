import math

a =int(input("Enter A :"))
b =int(input("Enter B :"))
c =int(input("Enter C :"))

tmp =(b**2)-(4*a*c)

part1_positive = (-b)+(math.sqrt(tmp))
part1_negative = (-b)-(math.sqrt(tmp))
part2 = 2 *a

print(f"result positive x : {part1_positive /part2}")
print(f"result negative x : {part1_negative /part2}")
