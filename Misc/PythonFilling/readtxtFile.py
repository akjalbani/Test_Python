''' example1 how to read txt file'''
file = open("data1.txt","r")
for line in file:
  print(line) # this will add an extra line
file.close()
