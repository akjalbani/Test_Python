# read a csv file and print or display output in a pretty tabular format.
# pip install prettytable 
# tested on repl.it
# @ AA Jalbani
# Date 24/02/2021 
# Version 1.0

from prettytable import from_csv
with open("one.csv",'r') as f:
  reader = from_csv(f)
print(reader)
