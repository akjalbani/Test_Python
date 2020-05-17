# draw a chees board (squares with adjacent square with different colors)
# with user input 
# list and condition to control the user input
# with exception handling
# this code demonstrates how loops are used in the programming, The concepts are illustrated using functions, 
#list, conditions, user_input an exception handling
# The code is tested in repl.it online python IDE 
# 
# draw a chees board (squares with adjusent square with different colors)
###########################################################################################################
# author: Akhtar Jalbani
# version: 1.0
###########################################################################################################
import turtle
turtle = turtle.Turtle()
################################################################################################
def Square_with_color(color):
  turtle.color(color)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(100)
    turtle.left(90)
  turtle.forward(100)
  turtle.end_fill()
################################################################################################
def draw_chessboard(color1,color2):
  y= 0
  for i in range(4):
    print("Outer Loop i: ",i)
    Square_with_color(color1)
    Square_with_color(color2)
    
    for j in range(2):
      print("--->Inner Loop j: ",j)
      Square_with_color(color1)
      Square_with_color(color2)
      
    turtle.penup()
    y = y + 100
    turtle.goto(0,y)
    turtle.pendown()
    color3 = color2
    color2 = color1
    color1 = color3
#############################################################################################   
colors = ["green","yellow","red","black","white","orange","blue"]
try:  
  color1 = input("Enter color1: ")
  color2 = input("Enter color2: ")
  if (color1 in colors) and (color2 in colors):
    draw_chessboard(color1,color2)
  else:
    print("choose correct color name: ")
except:
  print("Not a valid input")
##############################################################################################
