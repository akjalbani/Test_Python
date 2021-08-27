import requests
import sys

def check_url(url):
  try:
    h = {'user-agent':'firefox'}
    response = requests.get(url, headers=h)
    if response.status_code == 200:
      print(f'{url} is good!')
  except:
    print(f'{url} is bad')
    pass

check_url("https://www.google.com")
