#define a function for factorial
def fact(x):
    if x != 0 :
        return x * fact(x - 1)
    else:
        return 1
###  deriver program ####
m = int(input("Enter a positive number : "))
print("Number = ", m, " , factorail = ", fact(m))
