'''example 4: how to read names and ages separately from data2.txt file '''
file = open("data2.txt","r")
names = []
ages = []
for line in file:
  splitline = line.split(",") # split line based comma separator
  #print(splitline)
  names.append(splitline[0])
  ages.append(int(splitline[1]))  # you can use split but for int value, you can typecase to avoid any spaces
print(names)
print(ages)
file.close()
