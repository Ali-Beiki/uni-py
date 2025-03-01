input1 =int(input("Enter number first :"))
input2 =int(input("Enter number secound :"))

def isMultiple(first,secound) :
    if first % secound ==0 :
        return True
    else:
        return False
    
print(f"first number :{input1} ,secound number :{input2} ,is multiple {isMultiple(input1,input2)}")
      