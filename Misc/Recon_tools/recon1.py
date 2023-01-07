'''
This script allows the user to input a hostname or IP address, 
and then choose to either resolve the hostname to an IP, 
resolve an IP to a hostname, or scan for open ports. 
If the user chooses to scan for open ports, they can also specify a range of ports to scan.
'''
import socket

def get_ip(host):
  try:
    ip = socket.gethostbyname(host)
    return ip
  except:
    return "Unable to resolve hostname"

def get_hostname(ip):
  try:
    hostname = socket.gethostbyaddr(ip)
    return hostname
  except:
    return "Unable to resolve IP"

def scan_ports(host, start, end):
  try:
    open_ports = []
    for port in range(start, end+1):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.5)
      result = s.connect_ex((host, port))
      if result == 0:
        open_ports.append(port)
      s.close()
    return open_ports
  except:
    return "Error occurred during scan"

host = input("Enter a hostname or IP address: ")
choice = input("Enter 1 to resolve hostname to IP, 2 to resolve IP to hostname, or 3 to scan for open ports: ")

if choice == "1":
  print(get_ip(host))
elif choice == "2":
  print(get_hostname(host))
elif choice == "3":
  start = int(input("Enter the starting port number: "))
  end = int(input("Enter the ending port number: "))
  print(scan_ports(host, start, end))
else:
  print("Invalid choice")
