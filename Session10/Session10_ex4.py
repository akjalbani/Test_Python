'''Write a Python class to reverse a string word by word.'''
class ReverseString:
  def __init__(self,mystring):
    self.mystring= mystring
  def reverse_string(self):
    #return ' '.join(self.mystring.split(' ')[::-1])  # this is also one way
    # another way
    words = self.mystring.split() 
    words = list(reversed(words))
    return " ".join(words)

user_message = input("Type here ===> ")

obj = ReverseString(user_message)
print(obj.reverse_string())
