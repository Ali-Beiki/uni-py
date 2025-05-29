import pandas as pd
df1 = pd.DataFrame([['C programming',  130000 ],
                    ['C++ Programming', 110000],
                    ['Operating systems',  130000 ],
                    ['Java Programming', 120000]],
                   index=['0', '1', '2', '3'],
                   columns=['Book Title', 'Price'])
df1.to_excel("d:\output.xlsx")

