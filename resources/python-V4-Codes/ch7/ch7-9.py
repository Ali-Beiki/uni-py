class complex:
    def __init__(self, real, magic):
        self.real = real
        self.magic = magic
    #-------------------------------
    def __add__(self, other):
        return self.real + other.real, self.magic + other.magic
    def __sub__(self, other):
        return self.real - other.real, self.magic - other.magic
    def __eq__(self, other):
        return self.real == other.real and self.magic == other.magic
    def __mul__(self, other):
       return self.real * other.real, self.magic * other.magic 
    def __str__(self):
        return self.real, self.magic
    #---------------------------------
ob1 = complex(10, 18)
ob2 = complex(7, 11)
ob = ob1 + ob2
print("Sum of objects is :", ob)
ob = ob1 - ob2
print("Minus of objects is :", ob)
if (ob1 == ob2):
    print("Two object are equal ")
else :
    print("Two objects are not equal")
ob = ob1 * ob2
print("Multiply of objects is :", ob)
    
