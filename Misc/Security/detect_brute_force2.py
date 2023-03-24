'''This code prompts the user to enter a username and password, and checks if the credentials are correct. 
If the credentials are incorrect, the code records the failed attempt with the current timestamp in a dictionary. 
If the number of failed attempts from the same IP address exceeds a certain threshold (MAX_ATTEMPTS), 
the code blocks the IP address for a period of time 
(TIME_PERIOD) before allowing further login attempts.'''

import time

MAX_ATTEMPTS = 5  # maximum number of login attempts
TIME_PERIOD = 10  # time period in seconds

failed_attempts = {}  # dictionary to store failed attempts with timestamps

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # check if there are too many failed attempts from this IP
    ip_address = request.remote_addr  # get the IP address of the request
    if ip_address in failed_attempts:
        if len(failed_attempts[ip_address]) >= MAX_ATTEMPTS:
            # block the IP address for a period of time
            print("Too many failed login attempts. Please try again later.")
            time.sleep(TIME_PERIOD)
            continue

    # check if the username and password are correct
    if check_credentials(username, password):
        print("Login successful.")
        break
    else:
        print("Incorrect username or password.")
        # record the failed attempt with the current timestamp
        if ip_address not in failed_attempts:
            failed_attempts[ip_address] = []
        failed_attempts[ip_address].append(time.time())

