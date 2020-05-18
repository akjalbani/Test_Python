'''Q5 while loop'''
''' Calculate the sum and average of first n natural numbers using while'''
#####################################################################################

sum = 0
count = 0
n = 1
while n<=10:
    sum= sum + n # sum the adjacent values
    count = count+1 # count the number of values
    n = n+1

print("Sum = ", sum) # print sum
print("Average = ",sum/count) # calcualte and print the avg

#####################################################################################
'''Q5 for loop'''
''' Calculate the sum and average of first n natural numbers using for loop'''
sum = 0
count = 0
for i in range(1,11):
    sum= sum + i # sum the adjacent values
    count = count+1 # count the number of values
    

print("Sum = ", sum) # print sum
print("Average = ",sum/count) # calcualte and print the avg
