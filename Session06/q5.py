'''
  Q5 Write a Python function to check whether a string is a pangram or not. 
  Note :Pangrams are words or sentences containing every letter of the alphabet at least once.
  For example : "The quick brown fox jumps over the lazy dog"
'''

def isPanagram(str1):
  str1 = set(str1) # remove duplicates 
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet = set(alphabet) 
  if alphabet <=str1:
    return True
  else:
    return False


str1 = 'The quick brown fox jumps over the lazy dog'

if isPanagram(str1.lower()):
  print("This is a panagram")
else:
  print("This is not a panagram")
