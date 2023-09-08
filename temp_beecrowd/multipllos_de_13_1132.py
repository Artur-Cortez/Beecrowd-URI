soma, passo = 0, 1

x = int(input())

y = int(input())

if x > y: 
  passo = -1
  y -= 1
else:
  y += 1

for i in range(x, y, passo):
  if i % 13 != 0: soma += i
print(soma)
