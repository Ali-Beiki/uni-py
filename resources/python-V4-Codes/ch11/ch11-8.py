import pandas as pd
df1 = pd.read_excel("d:/Student.xlsx")
df1 .loc[4,['Grade']] = 15.5
df2 = pd.DataFrame([['Mohammad',  101, 17],
                    ['Navid', 102, 14],
                    ['Saman',  103, 16 ],
                    ['Javan', 104, 15.5]],
                   index=['0', '1', '2', '3'],
                   columns=['Name', 'StNo', 'Grade'])
df1 = df1.append(df2, ignore_index = True)
df1.to_excel("d:/NewStudent.xlsx")

