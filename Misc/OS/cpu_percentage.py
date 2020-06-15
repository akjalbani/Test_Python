# health of operating system
# this will show you the percentage of cpu usage 
# psutil library is used to cpu in python
# if not installed you should install first with pip command > pip install psutil
# tested on python IDLE
# author: AAJ
# 15-05-2020

import psutil
cpu_usage = psutil.cpu_percent(0.5) # cpu at 0.5 sec , this is set at 0.5 sec, every time you run you will get different value
print("cpu percenatge: ", cpu_usage) 


