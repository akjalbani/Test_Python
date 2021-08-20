## using user defined function - ping any ipaddress

def ping(ipAddress):
    response = os.popen("ping {}".format(ipAddress))
    if "Received = 4" in response:
        return True
    else:
        return False

userip = input("Enter Ip address -> ")
if ping(userip):
    print("ping of {} is successful".format(userip))
else:
    print("ping of {} is unsuccessful".format(userip))
    
    
