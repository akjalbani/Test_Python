# This is code is the extension of the encrypted message to decrypt your encrypted message
# First run the encrypted program to generate the encrypted message with key for example key=3 and message = hello -> 
# encrypted message becomes khoor
# Now run  decryptedMessage program with key =3 and encrypted message: khoor, you will get the out as hello
# source: https://projects.raspberrypi.org/en/projects/secret-messages-cc/1

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input("Enter decryption Key: "))
newMessage =''
message = input('Please enter a encrypted message: ')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position-key) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is: ',newCharacter)
        newMessage += newCharacter
    else:
        newMessage += newCharacter
print("Your message: ", newMessage)
