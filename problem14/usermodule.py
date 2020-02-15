def collatz(n):
  print(n)
  collatz.count +=1
  if (n==1):
    return True
  elif (n%2==0):
    n = n/2
  else:
    n = 3*n+1
  collatz(n)

def collatzLen(n):
  collatz.count = 0
  collatz(n)
  return(collatz.count)

# maxVal = 1
# term = 0
# collatzLen(100)
# for i in range(1000000):
#   i = 1000000-i
#   if(collatzLen(i)>maxVal):
#     maxVal = collatzLen(i)
#     term = i
#     print(i,":",maxVal)

# print(term)
# print(maxVal)



