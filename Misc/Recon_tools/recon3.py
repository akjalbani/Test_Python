'''
The main difference between this version and the previous one is the 
use of a with statement to manage the socket. This ensures that the socket 
is closed properly when the block of code is exited, whether due to completion or an exception. 
This can help to prevent resource leaks and improve the efficiency of the code.
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
  open_ports = []
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(0.5)
      for port in range(start, end+1):
        result = s.connect_ex((host, port))
        if result == 0:
          open_ports.append(port)
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
