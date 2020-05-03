'''2.	Write a python program to read numbers ‘a’ and ‘b’. Check whether a is divisible by b. '''
a = int(input("Enter value of a -> " ))
b = int(input("Enter value of b -> " ))

if a % b == 0:
  print("{} is divisible by {}.".format(a,b))
else:
  print("Sorry {} is not divisible by {}.".format(a,b))

  
