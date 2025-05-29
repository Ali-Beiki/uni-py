class person:
    def __init__(self, name = "", idnumber = 0):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("{0:10s} {1:<5d}".format(self.name, self.idnumber), end = "")
#--------------------------------------
class student(person):
    def __init__(self, name, idnumber, stno, ave):
        person.__init__(self, name, idnumber)
        self.stno = stno
        self.ave = ave
    def isExcelent(self):
        return self.ave >= 17
    #-----------------------------------
    def display(self):
        super().display()
        print("{0:<5d}  {1:9.2f}".format(self.stno, self.ave))
        
