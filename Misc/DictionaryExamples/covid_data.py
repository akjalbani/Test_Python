# This example is the practical demonstration of the nested dictionaries- live covid-19 data set is used for the learning purpose
# @Author: AAJ
# Date 31/05/2020
# Version 0.1
# Tested on repl.it


import requests
import json
response = requests.get('https://pomber.github.io/covid19/timeseries.json').json()

# check the data type of the data retrieved from the github, json must be dict type
#print(type(response))
#print(response.keys()) # find the keys
# from keys we found that country name is key
#print(response['Australia'])
# we can check the result and found that the country key contains data which looks likes as a dictionary in the list
# {'date': '2020-4-2', 'confirmed': 9, 'deaths': 0, 'recovered': 0}
#print(response['Australia'])
currentValue = len(response['Australia']) -1 # total values in the Australia
print("Country: Australia")
print("Date: ",response['Australia'][currentValue]['date'])
print("Confirmed Cases: ",response['Australia'][currentValue]['confirmed'])
print("Deaths: ",response['Australia'][currentValue]['deaths'])
print("Recovered: ",response['Australia'][currentValue]['recovered'])
