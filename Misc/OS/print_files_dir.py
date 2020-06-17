# tested on python IDEL

import os
count =0
for root, directories, files in os.walk("/"):
    # print the root of the directory
    print(root)
    # print the directories within the root
    print(directories)
    # print the files within the root
    print(files)
    # if we don't break the loop, it will print each and every file, directory.
    count = count + 1
    if count > 10:
        break
