##Sample JSON Format to describe details and display the information
### 
device_info = {
    "routers": [
      {
        "name": "CSR1000V",
        "vendor": "Cisco",
        "type": "virtual"
      },
      {
        "name": "1921",
        "vendor": "Cisco",
        "type": "hardware"
      }
    ]
}
print("Router Information")
print("==============")
print("Name: ", device_info["routers"][0]["name"])
print("Vendor: ", device_info["routers"][0]["vendor"])
print("Type: ", device_info["routers"][0]["type"])
print("-------")
print("Name: ", device_info["routers"][1]["name"])
print("Vendor: ", device_info["routers"][1]["vendor"])
print("Type: ", device_info["routers"][1]["type"])
