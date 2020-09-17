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

  
  ##################################################################
  # Another solution from my student: Jillian Davis 202020
  #author: Jillian Davis
  # dated: 17/09/2020
  ##################################################################
  
 string = "the quick brown fox jumps over the lazy dog".split()
unique_words = []
word_counts = []
for word in string:
  if word not in unique_words:
    unique_words.append(word)
    word_counts.append(1)
  else:
    word_counts[unique_words.index(word)] += 1
for i in range(len(unique_words)):
  print(unique_words[i], word_counts[i])
