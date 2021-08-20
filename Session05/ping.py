## Tested on IDLE

import os
response = os.popen("ping 8.8.8.8").read()
print(response)
if "Received = 4" in response:
    print("Ping is successfull")
else:
    print("Ping is unsuccessfull")





