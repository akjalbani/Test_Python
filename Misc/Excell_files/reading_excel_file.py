# load any excel_file
# filename.xlsx
# if pandas is not installed use commdand to install pandas - pip install pandas
# tested on python IDLE

import pandas as pd
excel_filename = input("Enter file name : -> ")
df= pd.read_excel(excel_filename)
print(df)
