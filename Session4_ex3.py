'''3.	A factorial is a number calculated by multiplying a non-negative integer with itself and all its preceding integers. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120. Write a script to ask the user for a number and calculate its factorial. As an extension, validate the input provided, and make your program keep asking for input if the user does not provide a non-negative integer when asked. '''

while True:
  n=int(input("Enter the number or 0 to exit: "))
  if n==0:
    break
  fact=1
  if n > 0:
    for i in range(1,n+1):
      fact=fact*i
      
  else:
    print("factorial doesn't exist for negative numbers")
    n=int(input("Enter the number: "))
  print("{}! = {}".format(n,fact))
  
