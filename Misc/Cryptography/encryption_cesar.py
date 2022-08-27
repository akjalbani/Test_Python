# This is simple python implementation of cesar cypher algorithm
# simple encryption techniques by replacing each char by fifth element from alphapbet
# for example b will be converted to g ( i.e after b fifth element wil be g)
# plaintext = ciphertext +5
# @author: A.A.J dated: 27/8/2022
import string
char = string.ascii_letters
print(char)
ciphertext = ""
plaintext = input(">>")
for c in range(len(plaintext)):
  for i in range(len(char)):
    if plaintext[c] == char[i]:
      i = i + 5
      ciphertext= ciphertext+char[i]
print(ciphertext)

