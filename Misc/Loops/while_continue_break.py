while True:
  try:
    val = int(input("Please enter an integer: "))
  except:
    print("Looks like you did not enter an integer!")
    continue
  else:
    print("Yep that's an integer!")
    break
    
