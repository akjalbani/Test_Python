'''Q1'''
class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def area_of_rectangle(self):
    return self.length*self.width

rect_object = Rectangle(4,5)
area = rect_object.area_of_rectangle()
print("Area of rectangle = ", area)
