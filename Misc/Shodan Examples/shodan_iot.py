'''shodan script to find vulnerablities in IoT devices. We search for webcamXP - Webcam and Network Camera Surveillance Software. 
webcamXP is the most popular webcam and network camera software for Windows. 
It allows you to monitor your belongings from any location with access to Internet by turning your computer into a security system.
 
 date: 20/9/2021
 python IDLE
 pip install shodan
 
'''
import shodan
from time import sleep

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
api = shodan.Shodan ( SHODAN_API_KEY )
query = 'webcamxp'
try :
    # Step 2 - Search using Shodan API
    results = api.search ( query )
    print ('Total number of results : {} '. format ( results ['total']) )
    for result in results ['matches']:
        # Step 3 - Print IP and country for every obtained result
        print ('IP: {} '. format ( result ['ip_str']) ) # The IP for each result is printed
        # print ( result [' data ']) # To print raw data for each result
        host = api.host(result['ip_str'])
        print ('- Country : {0} '.format( host.get('country_name', 'n/a')))
        print ('')
        sleep (1) # A 1- second delay is necessary to respect Shodan API restrictions

        # Step 4 - For each device IP , vulnerabilities and exploits are listed
        try :
            if str ( host.get('vulns')) != 'None':
                print (' -------------------- Exploit list --------------------')
                for vulnerability in host.get('vulns'):
                    exploits = api . exploits.search (vulnerability)
                    sleep (1)
                    print ('Found {0} exploits for vulnerability "{1}" \n'.format(exploits.get('total') , vulnerability ))

        except shodan.APIError as erro :
            print ( 'Error during exploit query : "{0}" '.format(query))
            print ('Shodan error : {0} '.format( erro ))

except shodan.APIError as e:
    print ('Error : {} '. format (e))

