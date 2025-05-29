import pandas as pd
data = pd.read_excel("d:/Student.xlsx")
print("All of rows:") 
print(data)
print("--------------------")
print("Rows with grade > 18")
df = data.loc[data['Grade'] > 18]
print(df)
