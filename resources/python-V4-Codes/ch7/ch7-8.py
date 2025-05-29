class base :
    def __init__(self) :
       self.num1 = 10
    def show(self) :
       print("show() in base class : num1 = ", self.num1)
#----------------------------------
class derived(base) :
    def __init__(self) :
        super().__init__()
        self.num2 = 30
    def show(self) :
        print("show () in derived class : num2 = ",
        self.num2)
# -------------------
# strat of main program
baseOb = base()
deriveOb = derived()
baseOb.show()
baseOb = deriveOb
baseOb.show()
