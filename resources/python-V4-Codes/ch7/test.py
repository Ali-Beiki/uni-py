class test:
    def __init__(self, a = 10, b = 20):
       self.x = a
       self.y = b
    def display(self):
        print("x = ", self.x, ", y = ", self.y)
## Driver program to test
ob1 = test()
ob1.display()
ob2 = test(15)
ob2.display()
ob3 = test(b = 25)
ob3.display()
ob4 = (24, 44)
ob3.display()
