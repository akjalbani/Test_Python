# This is simple square- demonstrated for function with paramters
# @ author: Akhtar Jalbani
import turtle
turtle = turtle.Turtle()
# function defination with parameter, we hard coded for left to make it 90 degrees for square and side length be changed
def square(x):
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(x)
  turtle.left(90)

# function call
square(100)
