'''4.	A school has following rules for grading system on the basis of marks obtained:
a. Below 25 - F
b. 25 to 44.9 - E
c. 45 to 49.9 - D
d. 50 to 59.9 - C
e. 60 to 79.9 - B
f. Above 80 - A
'''
#Write a python program to read the marks obtained by the user and print the corresponding grade.
marks_obtained = float(input("Enter your marks -> "))
student_name = input("Enter your name -> ")
if marks_obtained <25:
  print("Hey Mr. {}, your score is {} and your grade is F.".format(student_name,marks_obtained))
elif marks_obtained >=25 and marks_obtained <=44.9:
  print("Hey Mr. {}, your score is {} and your grade is E.".format(student_name,marks_obtained))
elif marks_obtained >=45 and marks_obtained <=49.9:
  print("Hey Mr. {}, your score is {} and your grade is D.".format(student_name,marks_obtained))
elif marks_obtained >=50 and marks_obtained <=59.9:
  print("Hey Mr. {}, your score is {} and your grade is C.".format(student_name,marks_obtained))
elif marks_obtained >=60 and marks_obtained <=79.9:
  print("Hey Mr. {}, your score is {} and your grade is B.".format(student_name,marks_obtained))
elif marks_obtained >=80 and marks_obtained <=100.0:
  print("Hey Mr. {}, your score is {} and your grade is A. ".format(student_name,marks_obtained))
elif marks_obtained >100:
  print("Sorry {} it is not a valid score ".format(student_name))
  
  
