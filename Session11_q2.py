'''Q2 Create the above file and name it  “School.txt”  Using the file school.txt, find the number of characters in the file and assign that value to the variable num_char.Also find the number of lines in the file by using Len method and for loop as well.'''
print("=======================Session-11- Q2.=========================")
file = open("school.txt","r")  

#num_char = file.read()
num_lines = 0
num_words = 0
num_char = 0
for line in file:
    wordslist = line.split()
    num_lines = num_lines + 1
    num_words = num_words + len(wordslist)
    num_char = num_char + len(line)
print('# of Lines: ', num_lines)
print('# of Words: ', num_words)
print('# of Characters: ', num_char)

