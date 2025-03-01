input1 =int(input("Enter number first :"))
input2 =int(input("Enter number secound :"))
input3 =int(input("Enter number third :"))

def compare(a,b,c):
    tmp =a if a>b else b
    max = tmp if tmp>c else c
    return max

print(f"first number :{input1} ,secound number:{input2} ,third number :{input3} ,larg number :{compare(input1,input2,input3)}")