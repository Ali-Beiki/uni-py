class studentClass:
    def __init__(self, name = " ", stno = 0, ave = 0.0):
        self.name = name
        self.stno = stno
        self.__ave = ave
    def getAve(self):
        return self.__ave
    #------------------------------------------
    def display(self):
        print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
        print("{0:10s} {1:4d} {2:8.2f}".format(self.name, self.stno, self.__ave))
    #------------------------------------------
