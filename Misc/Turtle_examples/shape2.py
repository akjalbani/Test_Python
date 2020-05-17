# Turtle graphics- turtle will draw angle from 0-360 (15 deg) 
# tested in repl.it
# Type- collection and modified

import turtle
turtle = turtle.Turtle()

for angle in range(0, 360, 15):
  turtle.setheading(angle)
  turtle.forward(100)
  turtle.write(angle)
  turtle.backward(100)
  
  
