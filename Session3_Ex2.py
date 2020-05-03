'''2.	Write a script to check whether the number entered by user is even or odd?'''

user_input = int(input("Enter a number-> "))
# check number is even or odd
# for even numbers reminder must be zero
if user_input %2 == 0:
  print("{} is an even number".format(user_input))
else:
  print("{} is an odd number".format(user_input))
