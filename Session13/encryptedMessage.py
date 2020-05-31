# source: https://projects.raspberrypi.org/en/projects/secret-messages-cc/1
# follow the tutorial and following will be the final code for encryption of messages

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key =3
newMessage =''
message = input('Please enter a message: ')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is: ',newCharacter)
        newMessage += newCharacter
    else:
        newMessage += newCharacter
print("Your message: ", newMessage)
    
