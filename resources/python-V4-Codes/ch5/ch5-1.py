def enter(lst):
   while True : # infinity loop
      x = int(input("Enter a number, 0 to end : "))
      if x != 0 :
         lst.append(x)
      else :
         break
   ## end of while
#------------------------------
def negFunc(lst):
    print("\n Negatives are : ")
    neg = 0   #number of negatives
    for item in lst:
        if item < 0:
           print(item, " ", end = "")
           neg += 1
    print("\nNumber of negatives is : ", neg)
    ## end of for
#------------------------------
def posFunc(lst):
    pos = 0  #number positives
    print("\n Positives are : ")
    for item in lst :
       if item > 0 :
           print(item, " ", end = "")
           pos += 1
    print("\nNumber of positives is : ", pos) 
    ## end of for
#-----------------------------
def find(lst):
    x = int(input("Enter a number to search : "))
    if x in lst :
        print(x , " is in list.")
    else :
        print(x, " is not in list.")
#-----------------------------   
list1 = [] # empty list
enter(list1)
print(list1)
negFunc(list1)
posFunc(list1)
find(list1)



