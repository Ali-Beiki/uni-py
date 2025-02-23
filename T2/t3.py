countFuct =10
total =0
for i in range(1,countFuct+1):
    tmp =1
    for j in range(1,countFuct+1):
       if j<=i:
            tmp *=j
            print(j)
    print("----->",tmp)
    total += 1 / tmp

print(total)
