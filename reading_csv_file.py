import csv
with open('example.csv', newline='') as f:
  for row in csv.reader(f): 
    print(row)
