# email extractor, this program gets user input as email address and then process to extract lastname. firstname and email addresses, domain and orgnization name
#  Version 1.0
# # author: AAJ



# the input format for email mustbe dot between the names such as fname.lname@example.com
emailaddress = input("Enter email address-> ")
list_address=emailaddress.split("@", 1) # this split string into list based on the @ sign
username = list_address[0] # username will be at index 0
domain = list_address[1] # domain will be at index 1
d = domain.split(".",2) # this works for email address such as fname.lname@example.com.au, if u have email such as fname.lname@example.com then change value from 2 to 1 in split function 
org = d[0] # name of the orgnization/ company will be at index 0
list_username=username.split(".", 1) 
firstname = list_username[0]
lastname = list_username[1]
print("^"*30)
print("Your Personal details")
print("^"*60)
print("you are working at ",org.capitalize())
print("your orgnization website: "+"www."+domain)
print("Your Last name : "+lastname)
print("Your First name : "+firstname)
print("Your Email address: "+emailaddress)
print("^"*60)
