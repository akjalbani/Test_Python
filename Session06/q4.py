
"""
Q4 Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal
Each number is the two numbers above it added together
"""

def pascal_triangle(num):
  lst = [1]
  for i in range(num):
    print(lst) 
    new_lst = []
    new_lst.append(lst[0])
    for i in range(len(lst) - 1):
      new_lst.append(lst[i] + lst[i+1])
    new_lst.append(lst[-1])
    lst=new_lst
  return lst


num = int(input("Enter a number of rows of Pascal's triangle: "))
print(pascal_triangle(num))
