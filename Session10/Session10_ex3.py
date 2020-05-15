'''Q3. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle'''
import math
class Circle:
  def __init__(self,radius):
    self.radius = radius
  def area_of_circle(self):
    return math.pi*self.radius**2
  def perimeter_of_circle(self):
    return math.pi*2*self.radius

obj = Circle(4)
area = obj.area_of_circle()
perimeter = obj.perimeter_of_circle()

print("Area of Circle {:.2f} and perimeter is {:.2f}".format(area,perimeter))
