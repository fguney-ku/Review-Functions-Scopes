def ndigits(n):
  if n < 10:
    return 1
  else:
    return 1 + ndigits(n // 10)

print(ndigits(5))
print(ndigits(105))  
print(ndigits(15105))   

# write a recursive function to compute exponentiation: x**n

def exponentiate(x, n):
  global nCalls
  nCalls += 1

  if(n == 0):
    return 1
  else:
    return x * exponentiate(x, n - 1)


nCalls = 0
print(exponentiate(2, 5))
print(nCalls)


# slow when n is large
nCalls = 0
exponentiate(2, 500)
print(nCalls)

# can you do better than n+1 calls?

# if n is even, then x**n = (x**2)**(n/2)
# if n is odd, then x**n = x * (x**2)**((n-1)/2)

def exponentiate_faster(x, n):
  global nCalls
  nCalls += 1

  if(n == 0):
    return 1
  else:
    if n % 2 == 0:
      return exponentiate_faster(x**2, n/2)
    else:
      return x * exponentiate_faster(x**2, (n-1)/2)

nCalls = 0
exponentiate_faster(2, 500)
print(nCalls)