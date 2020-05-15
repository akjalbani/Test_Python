'''3.	Write a program to read a number 3-digit number. Extract the right most digit and print it. Extract the last 2 digits of the number and print it.'''

number = input("Enter 3 digit number ->")
if len(number) <3 or len(number) > 3:
  print("{} is not a 3 digit number".format(number))
else:
  number = int(number) # convert it into integer bwfore processing
  right_most_digit= number % 10  # rght most digit
  print("Right most digit of {} is {}".format(number, right_most_digit))

  last_two_digit= number % 100  #  last_two_digit
  print("Last two digits of {} is {}".format(number, last_two_digit))

  
# With Error Handling 
try:
  number = input("Enter 3 digit number ->")
  if len(number) <3 or len(number) > 3:
    print("{} is not a 3 digit number".format(number))
  else:
    number = int(number) # convert it into integer bwfore processing
    right_most_digit= number % 10  # rght most digit
    print("Right most digit of {} is {}".format(number, right_most_digit))

    last_two_digit= number % 100  #  last_two_digit
    print("Last two digits of {} is {}".format(number, last_two_digit))
except ValueError:
  print("Not a Valid Input")
  
