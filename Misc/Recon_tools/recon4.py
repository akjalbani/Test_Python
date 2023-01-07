'''
This script allows the user to input a hostname or IP address, 
and then choose one of four options: resolve the hostname to an IP, 
resolve an IP to a hostname, get whois information for a domain, or 
get the HTTP headers for a URL. The script makes use of the socket, 
whois, and requests modules to perform these tasks.

'''

import socket
import whois
import requests

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

def get_whois(domain):
  try:
    w = whois.whois(domain)
    return w
  except:
    return "Error retrieving whois information"

def get_headers(url):
  try:
    r = requests.get(url)
    return r.headers
  except:
    return "Error retrieving headers"

def main():
  host = input("Enter a hostname or IP address: ")
  choice = input("Enter 1 to resolve hostname to IP, 2 to resolve IP to hostname, 3 to get whois information, or 4 to get HTTP headers: ")

  if choice == "1":
    print(get_ip(host))
  elif choice == "2":
    print(get_hostname(host))
  elif choice == "3":
    print(get_whois(host))
  elif choice == "4":
    print(get_headers(host))
  else:
    print("Invalid choice")

if __name__ == "__main__":
  main()
