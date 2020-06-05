# simple use of string and loops
import time
str1 = "to everyone who is learning python right now, with enough practice you too can create a masterpiece like this."
words = str1.split()
while True:
  for word in words:
    print(word.upper())
    time.sleep(0.5)
