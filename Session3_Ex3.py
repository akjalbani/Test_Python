'''3.	Write a Python program to find those numbers which are divisible by 7 and multiple of 5.'''
# for example 35 is divisible by 7 ( 35%5 == 0) and it is also multiple of 5 ( 35%5==0)

user_input = int(input("Enter a number-> "))
# check divisible by 7 and 5
if user_input %7 == 0:
  if user_input % 5 == 0:
    print("Perfect {} is a divisible by 7 and multiplier of 5".format(user_input))
  else:
    print("Sorry {} is divisible by 7 but not multiplier of 5".format(user_input))
else:
  print("Sorry {} is not divisible by 7 ".format(user_input))
