'''example 5: how to read names and ages separately from data3.txt file '''
file = open("data3.txt","r")
names = []
ages = []
subjects=[]
for line in file:
  splitline = line.split(",") # split line based comma separator
  #print(splitline)
  names.append(splitline[0])
  ages.append(int(splitline[1]))  # you can use split but for int value, you can typecase to avoid any spaces
  subjects.append(splitline[2].strip())
print(names)
print(ages)
print(subjects)

#let us take input from user:
select = int(input("Choose a teacher:-> "))
print("Teacher Name: {}".format(names[select]))
print("Age : {}".format(ages[select]))
print("Subject : {}".format(subjects[select]))
file.close()
