sumSq = 0
total = 0
sqSum = 0

for num in range(1,101):
  print(num)
  sumSq += num**2
  print(sumSq)
  total += num
  sqSum = total **2
  print(sqSum)
  print(sqSum-sumSq)
