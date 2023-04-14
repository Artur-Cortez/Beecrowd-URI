C, R, S = 0, 0, 0
n = int(input())
for i in range(n):
  q, a = input().split()
  q = int(q)
  if a == "C":
    C += q
  elif a == "R":
    R += q
  elif a == "S":
    S += q
total = C + R + S
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {C}')
print(f'Total de ratos: {R}')
print(f'Total de sapos: {S}')
print(f'Percentual de coelhos: {(C/total * 100):.2f} %')
print(f'Percentual de ratos: {(R/total * 100):.2f} %')
print(f'Percentual de sapos: {(S/total * 100):.2f} %')