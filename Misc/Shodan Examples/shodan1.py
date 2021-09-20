''' This is a simple python script to use shodan search to find vulnerbilities 
Task: dispaly total search results, IP addresses, location and port number. 
Tested on python IDLE
To do list before work on this script
1. install shodan module using pip install shodan
2. signup for shodan.io account 
3. copy your shodan API key
author: AAJ
Date: 19/9/2021
'''
import shodan
api = shodan.Shodan('YOUR_SHODAN_API_KEY')


try:
    
    #search keyword to find vulnerbaulities
    # here we are searching for apache software related vulnerabilities.
    results = api.search('apache')
    
    #show results
    print("Result found", results['total'])
    print("----------------------")
    for result in results['matches']:
        IP = result['ip_str']
        CC = result['location']['country_name']
        PORT = result['port']
        print("IP: ", IP)
        print("Location: " , CC)
        print("open ports: ", PORT)
        
        
        #print(result['data'])
        print("----------------------")
except shodan.APIError as e:
    print('Error : {} '. format (e))
