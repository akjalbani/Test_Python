'''Example 2 Have a fun writing file'''

import random

answer = 0
points = 0

print("During this program, enter -1 to quit!")
name = input("Please enter your name:-> ")
while answer !=-1:
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)

  answer = int(input("what is "+str(num1)+" + "+str(num2)+"?\n"))

  if answer == num1 + num2:
    points +=1

  print("You currently have "+str(points)+" points.")


file = open("points.txt","a")
file.write(name+", your points ="+str(points))
file.write("\n")
file.close() 
