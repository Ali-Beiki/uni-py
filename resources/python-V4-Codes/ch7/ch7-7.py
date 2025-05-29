class c1 :
    def __init__(self) :
        self.num1 = 10
    def show(self) :
        print("show() in class c1 : num1 = ", self.num1)
# -------------------------------------
class c2 :
    def __init__(self) :
        self.num2 = 20
    def show(self) :
        print("show() in class c2 : num2 = ", self.num2)
# ---------------------------------------
class d(c1, c2) :
    def __init__(self) :
        c1.__init__(self)
        c2.__init__(self)
        self.num3 = 30
    def show(self) :
        c1.show(self)
        c2.show(self)
        print("in class d: ")
        print("num1 = ", self.num1, ", num2 = ",
              self.num2 , ",num3 = ", self.num3)
# -----------------------------------------
# strat of main program
ob = d()
ob.show()
