# 
# @Author: AAJ
# Date 31/05/2020
# Version 0.1
# Tested on repl.it

import requests
import json

response = requests.get('https://pomber.github.io/covid19/timeseries.json').json()
country= input("Enter Country Name: ")
country = country.capitalize()
currentValue = len(response['Australia'])-1 # total values in the Australia
print("Country: ",country)
print("Date: ",response[country][currentValue]['date'])
print("Confirmed Cases: ",response[country][currentValue]['confirmed'])
print("Deaths: ",response[country][currentValue]['deaths'])
print("Recovered: ",response[country][currentValue]['recovered'])
