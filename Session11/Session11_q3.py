#3.	Write a Python program to assess if a file school.txt is closed or not.

file1= open("school.txt","r")
file1.close()
if file1.close() == None:
  print("File is closed")
else:
  print("File is still opened")
