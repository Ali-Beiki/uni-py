# 1+2+3+4+5+....n
n =int(input("Enter number n :"))

def sum(n) :
    if n ==1:
        return 1
    else :
        return n + sum(n-1)
    
print(f"sum 1 to {n} = {sum(n)}")


