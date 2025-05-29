import pandas as pd
file = ('d:/Student.xlsx')
with pd.ExcelFile(file) as x:
     s1 = pd.read_excel(x, 'Sheet1')
     s2 = pd.read_excel(x, 'Sheet2')

print("Sheet 1:")
print (s1)
print("")
print("Sheet 2:")
print (s2)
