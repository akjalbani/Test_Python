''' Q1 - Can you write a script to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char itself.Sample String : 'restart'Expected Result : 'resta$t'
'''

s1 = "restart"
# save first letter in a variable for later usage
first_letter = s1[0]
#print(first_letter)
# replace all occurances of r to $
s2 = s1.replace("r","$")
#print(s2)
# concatenate the first letter (r) with the string in s2 variable which replaces all r characters with $ ( $sta$t)
# we have to reproduce first r which is saved in first_letter, so we have to start s2 from second position r+sta$t
print(first_letter + s2[1:])
