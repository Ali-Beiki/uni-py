## Driver program to test
from studentClassModule import studentClass
st1 = studentClass()
st2 = studentClass()
n = int(input("Enter number of student: "))
for i in range(n):
    name, stno, ave = input("Enter name, stno, ave: ").split()
    st = studentClass(name, int(stno), float(ave))
    if st.getAve() > st1.getAve():
        st2 = st1
        st1 = st
    elif st.getAve() > st2.getAve():
        st2 = st
#----end of for ------------
print("Best student: ")
st1.display()
print("-" *30)
print("Second student: ")
st2.display()
