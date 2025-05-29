from fractions import Fraction
from math import gcd

class Rational :
    def __init__(self,numerator:int=0,denominator :int =1)-> None:
        if denominator ==0 :
            raise ValueError("Denominator Not Ziro !")
        
        common = gcd(numerator,denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self,other) :
        if isinstance(other,Rational):
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented
    
    def __sub__(self,other) :
        if isinstance(other,Rational):
            new_num = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented
    
    def __mul__(self,other) :
        if isinstance(other,Rational):
            return Rational(self.numerator *other.numerator, self.denominator* other.denominator)
        return NotImplemented
    
    def __truediv__(self,other):
        if isinstance(other,Rational):
            return Rational(self.numerator *other.denominator, self.denominator* other.numerator)
        return NotImplemented

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

nums1 = Rational(1,2)
nums2 = Rational(1,3)

print(nums1 + nums2)
print(nums1 - nums2)
print(nums1 * nums2)
print(nums1 / nums2)

