# Simple turtle demo to write text on the screen use of for loop
# change the values to see the effects for left, forward, j and range
#@author: Akhtar Jalbani

import turtle
turtle = turtle.Turtle()
turtle.speed(5)
j = 0
for i in range(20):
  turtle.penup()
  j = j + 5
  turtle.forward(20+j)
  turtle.write("Hello World!")
  turtle.left(60)
  
