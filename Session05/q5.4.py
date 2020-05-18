'''Q4 ite a Python program to count the number of even and odd numbersfrom a series of numbers'''
numbers = [1,2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for i in numbers:
    if i%2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count+1
print("Total no. of Even numbers in the list = ",even_count)
print("Total no. of Odd numbers in the list = ",odd_count)
