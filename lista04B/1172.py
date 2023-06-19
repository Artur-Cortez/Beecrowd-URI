vetor = []
for i in range(10):
    a = int(input())
    vetor.append(a)
    if vetor[i] <= 0:
      vetor[i] = 1
    print(f'X[{i}] = {vetor[i]}')