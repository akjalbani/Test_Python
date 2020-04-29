def fact(n):
  result = 1
  while n > 1:
    result *= n
    n -= 1
  return result

print(fact(5))
print(fact(10))
print(fact(20))
