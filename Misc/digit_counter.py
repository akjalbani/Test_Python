line = input('Line: ')
count = 0
for c in line:
  if c.isdigit():
    count += 1
print('There are', count, 'digit(s).')
