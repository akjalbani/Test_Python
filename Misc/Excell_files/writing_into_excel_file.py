# tested on Python IDLE

import pandas as pd

df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
                         'physics': [68, 74, 77, 78],
                         'chemistry': [84, 56, 73, 69],
                         'algebra': [78, 88, 82, 87]
                         })

writer = pd.ExcelWriter('output.xlsx')
df_marks.to_excel(writer)
writer.save()
print('DataFrame is written successfully to Excel File.')


