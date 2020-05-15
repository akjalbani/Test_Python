class Animal:
  def __init__(self,name):
    self.name = name
  def talk(self):
    pass
class Dog(Animal):
  def talk(self):
    print("My dog " + self.name + " talking as: "+"WOOF WOOF")
class Cat(Animal):
  def talk(self):
    print("My cat " + self.name + " talking as: "+"MEOOOW")

d = Dog("Sheefoo")
d.talk()
c = Cat("Kitty")
c.talk()
