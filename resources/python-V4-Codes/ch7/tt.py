class person:
    def __init__(self, name = "", idnumber = 0):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("{0:10s} {1:5d}".format(self.name, self.idnumber))
#-----------------------------------
class student(person):
    pass
#--------------------
st = student("Ali", 1200)
st.display()
    
