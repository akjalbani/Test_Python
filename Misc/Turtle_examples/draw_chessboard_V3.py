# Chessboard v3 more improved version using nested loop ( added diffent color for adjacent squares)
# demosntration of nested for loop
#@author: Akhtar Jalbani
# 
import turtle
turtle = turtle.Turtle()
turtle.speed(10)
pos = 0
#######################################################
def square_color1(color):
  turtle.color(color)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(100)
    turtle.left(90)
  turtle.forward(100)
  turtle.end_fill()
#######################################################
color1 = "black"
color2="red"
for row in range(8):
  for col in range(4):
    square_color1(color1)
    square_color1(color2)
  color3 =color2
  color2 = color1
  color1 = color3
  turtle.penup()
  pos = pos+100
  turtle.goto(0,pos)
  turtle.pendown()
#######################################################
