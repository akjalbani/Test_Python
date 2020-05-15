'''Ex3.1 Write a python program to read the values of length and breadth of a rectangle from the user and check if it is square or not.'''

length = int(input("Enter length of Rectangle-> "))
breadth = int(input("Enter breadth of Rectangle ->"))
# for square both sides must be equal
if length==breadth:
  print("It is a Square")
else:
  print("Sorry! it is not Square")
