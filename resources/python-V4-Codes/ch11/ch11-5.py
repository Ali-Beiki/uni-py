import pandas as pd
df1 = pd.DataFrame([['C programming',  130000 ],
                    ['C++ Programming', 110000],
                    ['Operating systems',  130000 ],
                    ['Java Programming', 120000]],
                   index=['0', '1', '2', '3'],
                   columns=['Book Title', 'Price'])
df2 = pd.DataFrame([['Distributed Systems',  115000 ],
                    ['Database Security', 25000],
                    ['Network security',  130000 ],
                    ['Artificial intelligence', 110000],
                    ['Machine Learning', 140000]],
                   index=['0', '1', '2', '3', '4'],
                   columns=['Book Title', 'Price'])

with pd.ExcelWriter('d:\output2.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')
