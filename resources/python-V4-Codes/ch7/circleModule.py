import math
class circle:
    def __init__(self):
        self.__radius = 0
    #-----------------------
    def getRad(self):
        return self.__radius
    #-----------------------
    def setRad(self, radPar):
        self.__radius = radPar
    #-------------------------    
    def cirPerime(self):
        per = 2 * math.pi * self.__radius
        return per
    #-----------------------
    def cirArea(self):
        area = math.pi * self.__radius ** 2
        return area
    def  __del__(self):
        print("Destructor executed ")
    #-----------------------
