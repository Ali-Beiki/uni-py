#Driver program to test student class
from studentModule import student
st1 = student("ali", "ali@yahoo.com", 15.5)
print("First object:")
st1.display()
st1.sendemail()
st1.verify()
print("Second object:")
st2 = student("reza", "reza@yahoo.com", 18.5)
st2.display()
st2.sendemail()
st2.verify()
