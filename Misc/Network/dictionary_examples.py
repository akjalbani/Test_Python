# let us have list like this
devices = ['router1', 'juniper', '12.2']
print(devices)
############### Another way to print values #########################
for device in devices:
  print(device)
#If we build on this example and convert the list device to a dictionary, it would look like this:
devices = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
print(devices)
###########Print only keys#################################################
for device in devices: 
  print(device)  # this will print keys
###############Print only values #############################################
for v in devices.values():
  print(v)
##############print key and value##############################################
for device in devices:
  print(device,devices[device])  # print key and value
#####  OR####print key and value###############################################
for k,v in devices.items():
  print(k,v)

############################################ ##############################
### access any desired value pass the key
print("host name: "+ devices['hostname'])
print("host name: "+ devices['vendor'])
print("host name: "+ devices['os'])
#########################################################################
## how to get keys
print(devices.keys())
# how to get values
print(devices.values())
##################################################################
## How to add new value  - key and value- this will add as a last item in the dictionary
devices['location'] = "room2.31"
print(devices)
################################################################
## create new empty dictionary and add items to it
student = {}
student["id"] = 100232
student["name"] = "Michael"
student["class"] = "python"
student["year"] = 2020
print(student)
################################################################
# dictionary built in functions 
print(dir(dict))
###############################################################
# how to delete item
# pop() key to delete particualr key and value
student.pop('id')
print(student)
