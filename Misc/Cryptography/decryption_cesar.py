# This is simple python implementation of cesar cypher algorithm
# please see the encryption_cesar.py example for encryption, this is decryption code
# simple decryption techniques by replacing each char by fifth element from alphapbet
# for example g will be converted to b ( i.e after g fifth element wil be a in reverese order)
# plaintext = ciphertext  - 5
# @author: A.A.J dated: 27/8/2022
# plaintext = ciphertext -5  fpmyfw
import string
char = string.ascii_letters
print(char)
ciphertext = ""
plaintext = input(">>")
for c in range(len(plaintext)):
  for i in range(len(char)):
    if plaintext[c] == char[i]:
      i = i - 5
      ciphertext= ciphertext+char[i]
print(ciphertext)
