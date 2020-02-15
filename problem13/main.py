a = 0.009*50
print(a)
# print(int(str(a)[:4]))
print(1/50)

f = open('data.txt', 'r')
x = f.readlines()
f.close()

y = [[] for i in range(len(x))]

print("running")

for j in range(len(x)):
  x[j] = x[j].replace(" ", "")
  x[j] = int(x[j])

total = 0
for i in range(len(x)):
  total = total + x[i]

# print(total)
print(int(str(total)[:10]))
