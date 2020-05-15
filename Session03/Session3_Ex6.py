'''6.	A student will be allowed to take up the exam only if his/her attendance is more than 75%.
Write a python script to read the number of classes attended from the user, determine whether he/she is eligible or not. Number of classes held =50
Hint: attendance = (no attended/no held)*100
'''
name = input("Enter your name -> ")
number_of_classes_attended = int(input("How many classes you have attended -> "))
TOTAL_NUMBER_OF_HELD= 50   # constant value

attendance = (number_of_classes_attended / TOTAL_NUMBER_OF_HELD) * 100
# check eligibility 
if attendance >= 75.00:
  print("Congrats! Mr. {} you are eligible to sit in Exam, your attendence is {}%".format(name,attendance))
else:
  print("Sorry! Mr. {}, you are not eligible, your attendance is {}%".format(name,attendance))

