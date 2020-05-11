'''1.	Write a for loop to count from 1 to 20. Can you make it count in fours? Can you make it count backwards?'''
print("Count 1 to 20")
for i in range(1,21):
  print("{} ".format(i),end="")

# Can you make it count in fours?
print("\nCount in fours")
for i in range(4,21,4):
  print("{} ".format(i),end="")

print("\nCount backward")
for i in range(20,0,-1):
  print("{} ".format(i),end=" ")
