'''Example 3 Have a fun Reading and writing file- very useful to show the current state of the player- persistent programming'''
import random

answer = 0
try:
  file = open('points.txt','r')
  points = int(file.readline())
except:
  points = 0
print("You currently have "+str(points)+" points.")

print("During this program, enter -1 to quit!")
while answer !=-1:
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)

  answer = int(input("what is "+str(num1)+" + "+str(num2)+"?\n"))

  if answer == num1 + num2:
    points +=1

  print("You currently have "+str(points)+" points.")

file = open("points.txt","a")
file.write(str(points))
file.close() 
