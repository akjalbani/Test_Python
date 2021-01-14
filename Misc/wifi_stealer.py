# this is for learning purpose, do not use without permission
# this code will run on windows 10
# Tested on Python 3.8 - IDLE
# password will be saved in the pass.txt file
# Before using this script check on windows10 command prompt whether this command works on your Windows 10 OS  > netsh wlan show profile
# if netsh command works successfully, you can get the same result with this script.
# you can use pip to install subprocess and re modules
# from windows 10 command prompt :  > pip install subprocess 
#                                   > pip install re
# Dated: 14/1/2021
# @Akhtar
###################################################################################

import subprocess, re

cd1 = "netsh wlan show profile"
networks = subprocess.check_output(cd1, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)',networks.decode('utf-8'))
final_output =""
for network in network_list:
    cd2 = "netsh wlan show profile "+ network + " key=clear"
    result = subprocess.check_output(cd2,shell=True)
    final_output += result.decode('utf-8')

file = open("pass.txt","w")
file.write(final_output)
file.close()
    
