import platform,sys

if sys.platform == 'linux':
  print("You are running Linux operting system")
elif sys.platform == 'win32' or sys.platform == 'win64':
  print("You are running Windows operating system")
else:
  print("You are running Mac Operating system")
