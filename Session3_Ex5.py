'''5.	Write a python program to read the ages of 3 people and determine the oldest and the youngest among them.'''
# a,b,c 
# a>b and a>c -> a is the oldest
person1_name = input("Enter name of Person1 -> " )
person1_age = int(input("---Enter age of Person1 -> " ))

person2_name = input("Enter name Person2 -> " )
person2_age= int(input("---Enter age of Person2 -> "))

person3_name = input("Enter name of Person3 -> " )
person3_age = int(input("---Enter age of Person3 -> "))

if person1_age > person2_age and person1_age > person3_age:
  print("{} is older than {} and {}".format(person1_name,person2_name,person3_name))
elif person2_age > person1_age and person2_age > person3_age:
  print("{} is older than {} and {}".format(person2_name,person1_name,person3_name))
elif person3_age > person1_age and person3_age > person2_age:
  print("{} is older than {} and {}".format(person3_name,person1_name,person2_name))
else:
  print("All are of the same age")
