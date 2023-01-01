import re

# Define a list of search strings
search_strings = ["error", "warning", "critical"]

# Open the log file
with open("/path/to/log/file.log", "r") as f:
  # Iterate through each line in the file
  for line in f:
    # Use a regular expression to search for any of the search strings
    if re.search("|".join(search_strings), line):
      print(line)
