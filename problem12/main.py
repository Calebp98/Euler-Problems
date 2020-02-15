# # Find smallest number with 500 factors
# # 2*2*5*5*5 = 500
# # num of factors = (a+1)(b+1)...(e+1)
# # num = abc^4d^4e^4
# # num = 11*7*5^4*3^4*2^4
# # num = 62370000

# def ifTri(n):
#   a = int((2*n)**0.5)
#   return 0.5*a*(a+1) == n

# i = 62370000
# while(ifTri(i)==False):
#   i = i+1
# print(i)



# def tri(n):
#   total = 0
#   for i in range(n+1):
#     total += i
#   return total
# # print(tri(7))

# n = 10
# while(tri(n)!=i):
#   n = n+1
# print(n)

# def factor(n):
#   factors = []
#   nFac = 1
#   for i in range(int(n/2)):
#     i = i+1
#     if(n%i==0):
#       factors.append(i)
#       nFac = nFac+1
#   # factors.append(n)
#   # print(nFac)
#   return(nFac)
#   # return(factors)


# print(factor(tri(n)))
# # i = 11169

# while(factor(tri(i))<500):
#   i = i+1
#   # print(i,":",factor(tri(i)))
#   if(i%10 == 0):
#     print(i)
# print(i)

# # for i in range(10):
# #   i = i+1
# #   print(tri(i),":",factor(tri(i)))


from math import *

# Function to calculate the number of divisors of integer n
def divisors(n):
  limit = int(sqrt(n))
  divisors_list = []
  for i in range(1, limit+1, 1):
    if n % i == 0:
      divisors_list.append(i)
      if i != n/i:
        divisors_list.append(n/i)
  return len(divisors_list)
                
# Function to check for triangle number
def isTriangleNumber(n):
  a = int(sqrt(2*n))
  return 0.5*a*(a+1) == n

# Function to calculate the last term of the series adding up to the triangle number    
def lastTerm(n):
  if isTriangleNumber(n):
    return int(sqrt(2*n))
  else:
    return None

# First Step
# First number 'check' to have 500 divisors
check = 2**4 * 3**4 * 5**4 * 7 * 11

# Second Step
# Starting from 'check', iterate sequentially checking for the next 'triangle' number
while not isTriangleNumber(check):
  check += 1

# Third and Fourth Steps
# Calculate the last term of the series ('seriesLastTerm') that adds up to the newly calculated triangle number 'check'
seriesLastTerm = lastTerm(check)

# Iterate over triangle numbers checking for divisors > 500
while divisors(check) <= 500:
  # add the next term to check to get the next triangle number
  check += (seriesLastTerm + 1)
  seriesLastTerm += 1
print(check)