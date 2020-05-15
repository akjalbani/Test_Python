'''Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.'''

class ChangeCase:
  def getString(self):
    self.msg = input("Enter your message:-> ")
    return self.msg
  def convert_To_UpperCase(self,msg):
    return self.msg.upper()

obj = ChangeCase()
user_input =obj.getString()
print(user_input)
print(obj.convert_To_UpperCase(user_input))
