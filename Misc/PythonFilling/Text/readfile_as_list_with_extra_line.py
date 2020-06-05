'''example2 - add list to see how the extra line has been added '''
file = open("data1.txt","r")
names = []
for line in file:
  names.append(line)
print(names)  # you will see with each list item \n is added, we need to remove it
  
file.close()
