from  fractions import Fraction 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number(not zero): "))
com = complex(num1, num2)
frac = Fraction(num1, num2)
print("Complex number is : ", com)
print("Real part is: ", com.real)
print("Imaginary part is: ", com.imag)
print("Fraction is : ", frac)
print("Numerator : ", frac.numerator)
print("Denomirator: ", frac.denominator)


