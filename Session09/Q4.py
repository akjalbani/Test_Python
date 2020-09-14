'''Q4
Write a Python program to count the occurrences of each word in a given sentence:the quick brown fox jumps over the lazy dog
'''
s = "the quick brown fox jumps over the lazy dog"
count = dict() # create an empty dictionary
words = s.split() # spilt words from string
#print(words)
for word in words:
  if word in count:  # check if new dictionary has a duplicate word
    count[word] +=1   # increment count by one
   
  else:
    count[word] = 1  # else put every thing in the new dictionary
for k,v in count.items():
  print(k, "appears" ,v, "times")
