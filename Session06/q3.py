'''Q3 Write a Python function to check whether a number is in a given range.'''
''' suppose range(2,10) and get a number from the user and check wether it is in the range between 2,10 '''

def isInRange(n):
  if n in range(2,10):
    return True
  else:
    return False

number = int(input("Enter a number : "))

result = isInRange(number)
if result == True:
  print("The number {} is in the range".format(number))
else:
  print("The number {} is not in the range".format(number))
