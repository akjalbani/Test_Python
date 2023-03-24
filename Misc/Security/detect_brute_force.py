import time

# Dictionary to keep track of failed login attempts
failed_logins = {}

# Threshold for number of failed attempts within a time window
threshold = 5

# Time window (in seconds) to consider for brute force attack detection
time_window = 60

def detect_brute_force(ip_address):
    current_time = time.time()

    # Remove old entries from the dictionary
    for key in list(failed_logins.keys()):
        if current_time - key > time_window:
            del failed_logins[key]

    # Add the current login attempt to the dictionary
    if ip_address in failed_logins:
        failed_logins[ip_address] += 1
    else:
        failed_logins[ip_address] = 1

    # Check if the number of failed attempts exceeds the threshold
    if failed_logins[ip_address] > threshold:
        print(f"Possible brute force attack from {ip_address}")
        # Take appropriate action, such as blocking the IP address
