# open file for write data
f = open("test.dat", "w")
while True :
   st = input("Enter a student name : ")
   if st == "" :
       break
   f.write(st + "\n")
# end of while
f.close()
# open file for read data
f = open("test.dat", "r")
print("Contents of file is : ")
s = f.read()
while s != "" :
   print(s)
   s = f.read()
f.close()
