# This is simple way to generate password, you may have your own solution
# author: AAJ

import random

def generatePassword(length):
    password =''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+?><:0123456789'
    for c in range(length):
        password += random.choice(chars)
    return password

passwords=[]
while True:
    try:
        length = int(input("Enter password length > "))
        no_of_passwords = int(input("How many passwords you want to generate -> "))
        if length ==0 or no_of_passwords == 0:
            print("Bye Bye ... Length or number of passwords can not be zero")
            break
        else:
            for i in range(no_of_passwords):
                passwords.append(generatePassword(length))
           
            print(passwords)
        
    except:
        print("This is not valid input")

