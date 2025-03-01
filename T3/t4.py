input1 =int(input("Enter number first :"))

def revers(number):
    if number == 1:
        print (1)
    else :
        print(number)
        revers(number-1)
    
revers(input1)