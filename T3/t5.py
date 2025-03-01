list =[1,2,3,4,5,80,12,50]

def max(*numbers) :
    tmp =0
    for number in numbers :
       tmp = number if number > tmp else tmp
    return tmp
       

print(f"larg number in list {list} is :{max(*list)}")