# password generator

import string
import random

while True:
  password = string.ascii_letters+ string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
  password_length = int(input("Please provide length of the password: "))
  print("Password Length = {}".format(password_length))
  passwordList = []
  for passChar in range(password_length):
    passRandom = random.choice(password)
    passwordList.append(passRandom)

  result = "".join(passwordList)
  
  print("Password = {}".format(result))
  again = input("Do you want to repeat? (y/n) >")
  if again.lower() == 'y':
    continue
  elif again.lower() == 'n':
    break


