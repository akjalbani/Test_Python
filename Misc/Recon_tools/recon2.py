'''
This is the second version of the script uses threading to scan multiple ports concurrently, 
which can greatly reduce the time it takes to scan a large range of ports. 
It also includes a few minor changes to improve error handling and reduce 
the risk of the script crashing.
'''
import socket
import threading

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

def scan_port(host, port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    if result == 0:
      return port
  except:
    return

def scan_ports(host, start, end):
  open_ports = []
  threads = []
  for port in range(start, end+1):
    t = threading.Thread(target=scan_port, args=(host, port))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
    result = t.get_result()
    if result:
      open_ports.append(result)
  return open_ports

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

