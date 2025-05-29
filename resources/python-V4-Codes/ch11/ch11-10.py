import pandas as pd
#create dictionary
data = {
        'name': ['Saman', 'Kian', 'Amin', 'Linda'],
	'physics':   [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra':   [78, 88, 82, 87]
       }
#create dataframe from dictionary
df_marks = pd.DataFrame(data)
print('Original DataFrame')
print("--------------------------------------")
print(df_marks)
print("--------------------------------------")
df_marks.insert(4, "Computer", [80, 56, 70, 90])
print("New data frame after inserting a column: ")
print("--------------------------------------")
print(df_marks)
#You can write df_marks into an excel file
