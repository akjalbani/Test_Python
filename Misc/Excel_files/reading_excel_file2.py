# In this example, I am using studentlist.xlsx file saved on my desktop folder name excel_filling
# first I have accessed the folder using relative path os.chdir, excel and python file are saved the same folder
# Tested on pyton IDLE desktop
# openpyxl is not a default package, you need to install package using pip command
# how to install
#   ----> go to command propmt in windows and type pip install openpyxl
#  -----> pip install os ( if os package is not installed)
####################################################################
# studentlist.xlsx looks as follows:
''' 1234567891 | Tailor |Nilay |1234567891@abc.edu.au
1234567892 | Yelubayev |Rishat |1234567892@abc.edu.au
1234567893 | Agimi |Florim |1234567893@abc.edu.au
1234567894 | Campbell |William |1234567894@abc.edu.au
1234567895 | Ivancic |Peter |1234567895@abc.edu.au'''
####################################################################
import openpyxl
import os

os.chdir('C:\\Users\\xyz\\Desktop\\excel_filling')
workbook = openpyxl.load_workbook('studentlist.xlsx')
#print(type(workbook))
sheet = workbook.get_sheet_by_name('Sheet1')
#print(type(sheet))
#sheet_names = workbook.get_sheet_names()
#print(sheet_names)
sid = []
fname=[]
lname = []
email = []
length = len(sheet['A'])
# cell value start from 1 and array index start from 0, so we have to avoid 0 index, thats why range function started from 1.
for i in range(1,length):
       sid.append(sheet['A'+str(i)].value)
       fname.append(sheet['B'+str(i)].value)      
       lname.append(sheet['C'+str(i)].value)
       email.append(sheet['D'+str(i)].value)
print("Student Id|FirstName|LastName|Email Address ")
for p in range(len(sid)):
    print("{} | {} |{} |{}".format(sid[p],fname[p],lname[p],email[p]))
 
