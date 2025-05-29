def func1():
    print(msg)
#------------------
def func2():
    global msg
    msg = "I chaged in function 2"
    print(msg)
#---------------------
msg = "I like python programming"
func1()
func2()
print("After calling func2: ")
print(msg)
