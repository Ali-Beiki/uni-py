def genTrans():
    money =(10, 20, 30)
    return money
#-------------------------------
def sumTrans(trans):
    sum = 0
    for item in trans:
        sum += item
    print("Sum of transactions: ", sum)
#-Driver program -------------
trans = genTrans()
sumTrans(trans)
