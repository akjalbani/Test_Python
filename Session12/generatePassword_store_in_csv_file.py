# This small script will generate random password based on the user input -> no of passwords and the length of the password
# Store generated password into the CSV file
# author: AAJ

import random
import csv

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
            with open("mypass.csv","w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["SN", "Password"])
                for i in range(1,no_of_passwords+1):
                    new_password = generatePassword(length)
                    writer.writerow([i, new_password])
                    passwords.append(new_password )
            print(passwords)
            
    except:
        print("This is not valid input")
