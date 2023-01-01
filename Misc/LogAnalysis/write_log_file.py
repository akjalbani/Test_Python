import re

# Open the log file and the output file
with open("/path/to/log/file.log", "r") as log_file, open("output.txt", "w") as output_file:
  # Create a list to hold the matching lines
  matching_lines = []
  # Iterate through each line in the log file
  for line in log_file:
    # Use a regular expression to search for the string "error"
    if re.search("error", line):
      # Add the matching line to the list
      matching_lines.append(line)
  # Write the list of matching lines to the output file
  output_file.writelines(matching_lines)
