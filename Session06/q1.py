'''
  Q1. Write a Python function to sum all the numbers in a list.
  Sample List: [8, 2, 3, 0, 7]
  Expected Output: 20
'''

def sum(numbers):
  result =0
  for number in numbers:
    result=result + number
  return result

numbers = [8,2,3,0,7]
print("Sum = ", sum(numbers))

