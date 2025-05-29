##  Driver program to test 
from baseDeriveModule import * 
print("Enter name, idnumber, stno, ave of student :", end = " ")
name, idnumber, stno, ave = input().split()
st = student(name, int(idnumber), int(stno), float(ave))
print("Enter name, idnumber, salary of employee :", end = " ")
name, idnumber, salary = input().split()
em = employee(name, int(idnumber), int(salary))
st.display()
if st.isExcelent():
    print("The student is excelent ")
else:
    print("The student is not excelent ")
print("-" * 30)
em.display()    
