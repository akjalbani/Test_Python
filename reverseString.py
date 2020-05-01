def reverseString(user_string):
  ch = ''
  l = len(user_string)
  for i in range(l-1,-1,-1):
    ch = ch+ch.join(user_string[i])
  print(ch)

user_string = input("Enter your text:-> ")
reverseString(user_string)
