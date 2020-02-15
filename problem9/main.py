def isPythTri(a,b,c):
  if(a**2 + b**2 == c**2) and (a<b<c):
    # print(a^2 + b ^2)
    # print(c^2)
    # print(a,b,c)
    return True
  else:
    return False

print(isPythTri(3 ,4, 5))
print(isPythTri(3,4,6))
lim = 1000

for i in range(lim):
  for j in range(lim):
    for k in range(lim):
      if(i+j+k == 1000):
        if(isPythTri(i,j,k)):
          print(i,j,k)
          print(i*j*k)

