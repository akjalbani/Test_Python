# Q4 Write a Python program to combine each line from first file with the corresponding line in second file
# add some text in myfile.txt and take the previous school.txt and combine them line by line

with open('myfile.txt') as fh1, open('school.txt') as fh2:
  for line1, line2 in zip(fh1, fh2):
    print(line1+line2)
