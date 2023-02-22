from cryptography.fernet import Fernet

# Load the key used for encrypting the passwords
with open("key.txt", "rb") as file:
    key = file.read()
fernet = Fernet(key)

# Load the encrypted usernames and passwords from the file
with open("passwords.txt", "r") as file:
    data = file.readlines()
users = {}
for line in data:
    username, password = line.strip().split(":")
    users[username] = password.encode()

# Get username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered username and password match any of the pairs in the file
if username in users and fernet.decrypt(users[username]).decode() == password:
    print("Login successful!")
else:
    print("Incorrect username or password.")
