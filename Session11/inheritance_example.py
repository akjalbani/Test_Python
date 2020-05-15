class Person:
  def __init__(self,first,last):
    self.firstName = first
    self.lastName = last
  def Name(self):
    return self.firstName+" "+self.lastName
class Employee(Person):
  def __init__(self,first,last,staffNum):
    #Person.__init__(self,first,last)
    super().__init__(first,last)
    self.staffNumber = staffNum
  def getEmployee(self):
    return self.Name()+ " "+str(self.staffNumber)

x = Person("Mark","Telly")
y = Employee("Xin","Jin",1002323)

print(x.Name())
print(y.getEmployee())
