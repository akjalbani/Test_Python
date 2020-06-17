import os
filepath = "/tmp/my-temp-file.txt"
if os.path.isfile(filepath):
    os.remove(filepath)
else:
    print("Error: %s file not found" % filepath)
