'''Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.'''

class ChangeCase:
  def get_String(self):
    self.msg = input("Enter your message:-> ")
    return self.msg
  def toUpperCase(self,msg):
    return self.msg.upper()
     #print(self.msg.upper())

obj = ChangeCase()
user_input =obj.get_String()
print(obj.toUpperCase(user_input))
