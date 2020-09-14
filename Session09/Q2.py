'''Q2
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
(Hint:use the concept of slicing and swapping)Sample String : 'abc', 'xyz'Expected Result : 'xyc abz
'''

s1 = "abc"
s2 = "xyz"
s3 = s1+s2
print(s3)  
# Expected result is xyc abz
s = s2[:2] +  s1[2:] + " "+s1[:2] +s2[2:]
print(s)
