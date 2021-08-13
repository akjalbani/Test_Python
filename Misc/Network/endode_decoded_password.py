# This programs encode user password in base64 and decode using base64 module
# python module base64 and getpass are required
# tested on replit

import base64
import getpass


userlogin = input("Enter user name-> ")
userpassword = getpass.getpass("Enter pssword:")
utf_password = userpassword.encode("utf-8")
encoded_password = base64.b64encode(utf_password)

#print("User name - > ", userlogin)
#print("password -> ", encoded_password)
decoded = base64.b64decode(encoded_password).decode("utf-8")
#print("password -> ", decoded)
print("*"*30)

print("Let us verify username and pasword")
print("*"*30)
uname = input("User name:  ")
password = getpass.getpass("Password: ")
if uname == userlogin:
  if password == decoded:
    print("*"*30)
    print("Your username: {} and password = {}.".format(userlogin,encoded_password))
  else:
    print("*"*30)
    print("your passowrd is incorrect")
else:
  print("*"*30)
  print("your username is incorrecct")



