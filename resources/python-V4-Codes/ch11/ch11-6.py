import pandas as pd
cols = ['Name', 'Grade']
stGrade = pd.read_excel("d:/Student.xlsx", usecols = cols)
print(stGrade)
