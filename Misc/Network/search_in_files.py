#@author: A.A J
# Search a string in all files located in the current folder. 
# dated: 8/9/2021

import os
#1. Change path to current location and sort the files based on time
os.chdir('./')
files = sorted(os.listdir('.'),key=os.path.getctime, reverse=True)
#2. Get input from user 
userstr = input('Enter a keyword or string you want to search>>> ')
#3. check the string in each file when found print the file and string
for file in files:
    with open(file, 'r') as infile:
        for line in infile:
            if userstr in line:
                print(file,":", line)
