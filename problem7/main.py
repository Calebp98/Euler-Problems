

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

i = 0
num = 0
while(i<10001):
  if(isPrime(num)):
    print(i +1 , ":" , num)
    i = i+1
  num = num+1




