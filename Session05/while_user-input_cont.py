# Simple example to demonstrate the user_input until user decide to quit

import replit

while True:
  print(".......MENU OPTIONS.....................")
  print("\n[1] Enter 1 to input data")
  print("\n[2] Enter 2 to print data")
  print("\n[q] Enter q to Quit.")
  print("-------Select your choice----------------")
  choice = input("\nPlease enter a number between 1 and 2 or q to quit.")
  
  print("Your choice -> ", choice)
  
  if choice == '1':
    name = input("Enter your name: ")
    replit.clear()
  elif choice =='2':
    replit.clear()
    print("-------------OUTPUT-----------------")
    print("Your name is : "+ name)
  else:
    break
  
