# health of operating system
# shutil is used for disk usage , you can install using pip command > pip install shutil
# tested on pythonIDLE
# @author: AAJ
# v0.1
# 15-06-2020

import shutil
du = shutil.disk_usage("/")  
print(du)
# let us print percentage of free disk

free_dsk_per = du.free/ du. total * 100
print("Free Disk Space Percentage =",free_dsk_per)

