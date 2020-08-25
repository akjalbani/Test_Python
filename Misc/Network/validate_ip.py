def validate_ip(addr):
  a = addr.split('.')
  if len(a) != 4:
    return False
  for x in a:
    if not x.isdigit():
      return False
    i = int(x)
    if i < 0 or i > 255:
      return False
  return True
    
addr=input("Enter the IP address:")
address=validate_ip(addr)
if address:
    print('Valid IP')
else:
    print("Invalid IP")
