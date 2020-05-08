'''Write a Python class to reverse a string word by word.'''
class ReverseString:
  def __init__(self,mystring):
    self.mystring= mystring
  def reverse_string(self):
    return ' '.join(self.mystring.split(' ')[::-1])  

user_message = input("Type here ===> ")

obj = ReverseString(user_message)
print(obj.reverse_string())
