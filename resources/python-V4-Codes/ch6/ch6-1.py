def change(string):
    print("split the sting:")
    sp = string.split()
    print(sp)
    composite = ",".join(sp)
    print("Composite: ")
    print(composite)
    rep = composite.replace(",", ":")
    print("Replace: ")
    print(rep)
    subStr ="science" 
    index = string.find(subStr)
    if index == -1:
        print(subStr, " not found")
    else:
        print(subStr, " found at index ", index)
## Driver program ######
st = input("Enter a string :")
change(st)

