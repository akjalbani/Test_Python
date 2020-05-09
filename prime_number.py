try:
  num= int(input("Enter number ->"))

  for n in range(2,num):
    if num % n == 0:
      print(num,'is not prime')
      break
  else: # If never mod zero, then prime
    print(num,'is prime!')
except:
  print("Not a valid input")
