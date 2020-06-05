# you should run this script usig python Desktop IDE such as IDLE, pycharm .., online Editor repl.it may not support
# As loop is indefinte, you need forecfully close the python running script.
# This script is only for the learning purpose and expecting same from you to utilize the script for learing purpose not to harm others.
# author A.A Jalbani
# version 1.0
# Dated: 05/06/2020

import webbrowser
import time
import random

while True:
    sites = random.choice(["google.com","yahoo.com","bbc.com"])
    url ="http://{}".format(sites)
    webbrowser.open(url)
    seconds = random.randrange(5,20)
    time.sleep(seconds)
 
  
