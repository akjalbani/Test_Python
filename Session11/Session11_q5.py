'''Q5 create a csv file with Header row as id name and email as save it as employee.csv and 
store the contents in  a dictionary  also  print the email address of every employee '''
##############################################################
# first save your csv file as follows (employee.csv)
id,name,email
01,ABC,abc@abc.com
02,xyz,xyz@hxyz.com
############################################################

import csv
with open('employee.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      #print(row) # this line prints the header
      line_count += 1
    else:
      print("Id= {}, name = {} and email={} ".format(row[0],row[1],row[2]))
      line_count += 1
  #print("No of lines = ",line_count) # This will print number of lines in the csv file including header line
