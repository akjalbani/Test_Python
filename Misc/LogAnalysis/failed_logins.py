'''
This script will open the log file located at /path/to/log/file.log and search each line in the file for failed login attempts. 
It uses a regular expression to extract the IP address of the client that made the failed login attempt, and 
it keeps a count of the number of failed login attempts per IP address. 
If the number of failed login attempts for an IP address exceeds a specified threshold, 
the script will print a warning message indicating suspicious activity.

You can customize this script to meet the specific needs of your organization. 
For example, you could modify the regular expression to match different log entries or 
change the threshold for the number of failed login attempts. 
You could also add additional logic to take other actions, 
such as blocking the IP address or sending an alert to security personnel.

'''

import re

# Open the log file
with open("/path/to/log/file.log", "r") as f:
  # Set a threshold for the number of failed login attempts
  failed_login_threshold = 5
  # Initialize a dictionary to count the number of failed login attempts per IP address
  failed_logins = {}
  # Iterate through each line in the log file
  for line in f:
    # Use a regular expression to search for failed login attempts
    match = re.search(r"failed login from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
    if match:
      # Extract the IP address from the log entry
      ip_address = match.group(1)
      # Increment the count for the IP address
      if ip_address in failed_logins:
        failed_logins[ip_address] += 1
      else:
        failed_logins[ip_address] = 1
      # If the threshold for failed login attempts has been reached, print a warning
      if failed_logins[ip_address] >= failed_login_threshold:
        print(f"Suspicious activity detected from IP address {ip_address}")
