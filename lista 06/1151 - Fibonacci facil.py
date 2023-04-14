N = int(input())
fibs = [0, 1]
while len(fibs) < N:
  fibs.append(fibs[-1] + fibs[-2])
  
for i in range(N):
  if i == N-1:
    print(fibs[i], end="\n")
  else:
    print(fibs[i], end=" ")