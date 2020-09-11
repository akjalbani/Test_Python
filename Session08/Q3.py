#Q3  tuple1,tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200) Using max() method ,find the maximum valued element from these two tuples
# Contibutor : Engin

tuple1 = ("123", "xyz", "zara", "abc")
tuple2 = ("456", "700", "200")

x = tuple1 + tuple2
y = max(x)
print(y)
########################################
# solution 2: contributor : Akhtar
# Another solution for  tuple1,tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
# As we can not update or modify tuple, so we have to convert tuple to list and find maximum value
tuple1,tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
list1 = list(tuple1)
list2 = list(tuple2)
for i in range(len(list1)):
  if type(list1[i]) is int:
    list1[i] = str(list1[i])
for i in range(len(list2)):
  if type(list2[i]) is int:
    list2[i] = str(list2[i])
# convert it again to tuple

tuple1 = tuple(list1)
tuple2 = tuple(list2)
tuple3 = tuple1 + tuple2
#print(tuple3)
print("Max value in tuple1 and tuple2: ", max(tuple3))



