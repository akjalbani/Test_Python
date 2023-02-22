from cryptography.fernet import Fernet

# Generate a key for encrypting the password
key = Fernet.generate_key()
fernet = Fernet(key)

# Get username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Encrypt the password
encrypted_password = fernet.encrypt(password.encode())

# Save the username and encrypted password to a file
with open("passwords.txt", "a") as file:
    file.write(f"{username}:{encrypted_password.decode()}\n")

# Save the key to a file
with open("key.txt", "wb") as file:
    file.write(key)
