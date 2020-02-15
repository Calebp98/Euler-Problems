print("test")
f = open('data.txt', 'r')
x = f.readlines()
f.close()

y = [[] for i in range(len(x))]

print("running")

for j in range(len(x)):
  x[j] = x[j].replace(" ", "")
  for i in range(len(x[0])-1):
    if(i%2==0):
      # print(x[j][i:i+2])
      y[j].append(int(x[j][i:i+2]))
      # print(y[j])
# print(y)

def getProd(y):
  prod = 1
  for i in range(len(y)):
    prod = y[i] * prod
  return (prod)

products = []
maxProd = []

for j in range(len(y)):
  for i in range(len(y[0])-3):
    products.append(getProd(y[j][i:i+4]))
    # print(y[j][i:i+4])
maxProd.append(max(products))
products = []

for j in range(len(y)):
  col = [row[j] for row in y]
  for i in range(len(col)-3):
    # print("test")
    # print(i,j)
    # print(col[i:i+4])
    products.append(getProd(col[i:i+4]))
maxProd.append(max(products))
products = []
# print(maxProd)

for j in range(len(y)-3):
  for i in range(len(y[0])-3):
    diag =[y[j][i],y[j+1][i+1],y[j+2][i+2],y[j+3][i+3]]
    print(j,i)
    print(diag) # \
    products.append(getProd(diag))
maxProd.append(max(products))

for j in range(len(y)-3):
  j = j+3
  for i in range(len(y[0])-3):
    diag =[y[j][i],y[j-1][i+1],y[j-2][i+2],y[j-3][i+3]]
    print(j,i)
    print(diag)  
    products.append(getProd(diag))
maxProd.append(max(products))
print(maxProd)
print(max(maxProd))
