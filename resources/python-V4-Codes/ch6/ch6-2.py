def dicInsert(dic):
    state, center = input("Enter state, center :").split()
    dic[state] = center
#---------------------------------------------------
def dicSearch(dic):
    state = input("Enter state to search: ")
    if state in dic:
        print("{0:10s} {1:10s}".format("State", "Center"))
        print("{0:10s} {1:10s}".format(state, dic[state]))
    else:
        print("State ", state, " not found")
    input("Press a key to continue ! ") 
#---------------------------------------------------
def dicDisplay(dic):
    print("{0:10s} {1:10s}".format("State", "Center"))
    print("-" * 20)
    for state in dic:
        print("{0:10s} {1:10s}".format(state, dic[state]))
#---------------------------------------------------
def dicUpdate(dic):
    state, center = input("Enter state, center : ").split()
    d = {state:center}
    dic.update(d)
#---------------------------------------------------
def dicDelete(dic):
    state = input("Enter state to delete: ")
    if state in dic:
        del dic[state]
        print("State ", state, " deleted")
    else:
        print("State ", state, " not found")
    input("Press a key to continue ! ")
##Driver program ###
def menu():
    print("1. Enter data to dictionary ")
    print("2. Search a state ")
    print("3. Delete a state ")
    print("4. Update the state center")
    print("5. Display the contents of dictionary")
    print("6. Exit ")
    choice = int(input("Enter your select (1-6): "))
    return choice
#-------------------------
stdic = dict()
while True:
    c = menu()
    if c == 1:
        dicInsert(stdic)
    elif c == 2:
        dicSearch(stdic)
    elif c == 3:
        dicDelete(stdic)
    elif c == 4:
        dicUpdate(stdic)
    elif c == 5:
        dicDisplay(stdic)
    else:
        break

