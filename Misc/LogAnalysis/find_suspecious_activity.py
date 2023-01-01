'''
This code will open the log file located at /path/to/log/file.log and check each line in the file against a list of regular expressions
that match known patterns of suspicious activity. If the line does not match any of the patterns, it is considered suspicious 
and will be printed to the console.

You can customize the list of patterns to match different types of suspicious activity that you want to detect. 
You can also modify the script to take different actions when suspicious activity is detected, such as 
writing the matching lines to a file or sending an alert.

'''

import re

# Define a list of regular expressions to match suspicious activity
patterns = [
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\] \".+\" \d{3} \d+$",  # Valid HTTP request
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\] \".+\" \d{3} -$",  # Missing size in HTTP request
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\] \".+\"$",  # Missing size and status code in HTTP request
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\]$",  # Missing request in HTTP request
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - -$",  # Missing timestamp and request in HTTP request
]

# Open the log file
with open("/path/to/log/file.log", "r") as f:
  # Iterate through each line in the file
  for line in f:
    # Check if the line matches any of the suspicious patterns
    if not any(re.match(pattern, line) for pattern in patterns):
      print(f"Suspicious activity detected: {line}")
