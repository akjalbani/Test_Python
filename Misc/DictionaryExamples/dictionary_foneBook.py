phonebook = {}

line = input('Name and number: ')
while line:
  name, number = line.split()
  phonebook[name] = number
  line = input('Name and number: ')

print(phonebook)
