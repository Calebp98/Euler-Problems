def isPrime(n):
  i = 2
  if (n<=3):
    return n>1
  elif ((n%2==0)or(n%3==0)):
    return False
  i = 5
  while (i**2<=n):
    if ((n%i==0)or (n%(i+2)==0)):
      return False
    i = i+6
  return True


total = 0
for i in range(2000000):
  if(isPrime(i)):
    total+=i
print(total)
    