import pandas as pd
df = pd.DataFrame([['C programming',  130000 ],
                    ['C++ Programming', 110000],
                    ['Operating systems',  130000 ],
                    ['Java Programming', 120000]],
                   index=['0', '1', '2', '3'],
                   columns=['Book Title', 'Price'])
new_row = pd.DataFrame([['Distributed Systems',  115000 ]],
                    
                   index=['0'],
                   columns=['Book Title', 'Price'])
print("Original data frame:")
print(df)
print("------------------------------------")
df = pd.concat([new_row, df]).reset_index(drop = True)
print("New data frame with added a record at top: ")
print(df)

