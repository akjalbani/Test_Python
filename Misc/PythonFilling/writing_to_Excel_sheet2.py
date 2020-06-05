# This script demonstarte how to save data into excel work sheet, you need to install openpyxl using pip command --> pip install openpyxl
# @author: AA Jalbani
#  Version 1.0

import openpyxl
import os

workbook= openpyxl.Workbook()
sheet = workbook.create_sheet(index=0,title='Sheet1')
sheet['A1'] = "Student ID"
sheet['B1'] = "Last Name"
sheet['C1'] = "First Name"
sheet['D1'] = "Email"


sheet['A2'] = "4567891451"
sheet['B2'] = "Abc"
sheet['C2'] = "XYZ"
sheet['D2'] = "4567891451@abc.edu"


sheet['A3'] = "4567891452"
sheet['B3'] = "Aabb"
sheet['C3'] = "XYZAA"
sheet['D3'] = "4567891452@abc.edu"

os.chdir('C:\\Users\\xyz\\Desktop\\excel_filling') # path where to save excel file 
workbook.save("example1.xlsx")

