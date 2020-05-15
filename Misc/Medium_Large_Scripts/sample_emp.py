# This script is for learning purpose
import os
import platform
import replit

replit.clear()
global listEmp #Making ListEmp As Super Global Variable
listEmp = ["Mark", "Navy", "Edgar", "Rashi", "Rehab","Taylor","Paul","Pumi","Zoey"] #List Of Employees

def manageEmployee(): #Function 

	x = "#" * 30
	y = "=" * 28
	global bye #Making Bye As Super Global Variable
	bye = "\n {}\n# {} #\n# ===> Good Bye<===  #\n# ===> Script is for learning purpose <===  #\n# {} #\n {}".format(x, y, y, x) # Will Print GoodBye Message

	#Printing Welcome Message And options For This Program
	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Sample Employee Management System   	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Employee List 
Enter 2 : To Add New Employee 
Enter 3 : To Search Employee 
Enter 4 : To Remove Employee
		
		""")

	try: #Using Exceptions For Validation
		userInput = int(input("Please Select your choice: ")) #Will Take Input From User
	except ValueError:
		exit("\nHy! That's Not A Number") #Error Message
	else:
		print("\n") #Print New Line

	#Checking Using Option	
	if(userInput == 1): #This Option Will Print List Of Employees
		print("Employee List\n")  
		for employee in listEmp:
			print("=> {}".format(employee))

	elif(userInput == 2): #This Option Will Add New Employee In The List
		newEmp = input("Enter New Employee Name: ")
		if(newEmp in listEmp): #This Condition Checking The New Employee Is Already In List Ur Not
			print("\nThis Employee {} Already In The List".format(newEmp))  #Error Message
		else:	
			listEmp.append(newEmp)
			print("\n=> New Employee {} Successfully Add \n".format(newEmp))
			for employee in listEmp:
				print("=> {}".format(employee))	

	elif(userInput == 3): #This Option Will Search Employee From The List
		srcEmp = input("Enter Employee Name To Search: ")
		if(srcEmp in listEmp): #This Condition Searching The Emp
			print("\n=> Record Found Of Employee {}".format(srcEmp))
		else:
			print("\n=> No Record Found Of Employee {}".format(srcEmp)) #Error Message

	elif(userInput == 4): #This Option Will Remove Employee From The List
		rmEmp = input("Enter Employee Name To Remove: ")
		if(rmEmp in listEmp): #This Condition Removing The Employee From The List 
			listEmp.remove(rmEmp)
			print("\n=> Employee {} Successfully deleted \n".format(rmEmp))
			for employee in listEmp:
				print("=> {}".format(employee))
		else:
			print("\n=> No Record Found of This Employee {}".format(rmEmp)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): #Validating User Option
		print("Please Enter Valid Option")	#Error Message	
						
#brought to you by code-projects.org
manageEmployee()

def runAgain(): #Making Runable Problem1353
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageEmployee()
		runAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

runAgain()		
