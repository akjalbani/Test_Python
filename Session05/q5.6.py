'''Write a Python program to get the Fibonacci series between 0 to 50.'''
def fib(n):
  if n <=1:
    return n
  else:
    return fib(n-1)+fib(n-2)
    
for i in range(50):
    print(fib(i))
