'''
  Q2 Write a Python program to reverse a string.
  Sample String: "1234abcd"
  Expected Output: "dcba4321
'''

inString = input("Enter a string value-> ")
length = len(inString)
outString= ''
while length > 0:
  outString = outString + inString[length-1]
  length = length-1

print(outString)

