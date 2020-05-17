# simple shape to demonstrate for loop
# @author: Akhtar Jalbani
# Version=1.0

import turtle
turtle = turtle.Turtle()

for i in range(5):
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(100)
  turtle.goto(0,0)
turtle.right(200)
turtle.forward(400)
