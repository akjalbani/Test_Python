'''Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.'''

class ChangeCase:
  def get_String(self):
    self.msg = input("Enter your message:-> ")
    return self.msg
  def print_String(self,msg):
     print(self.msg.upper())

obj = ChangeCase()
user_input =obj.get_String()
print(user_input)
obj.print_String(user_input)
