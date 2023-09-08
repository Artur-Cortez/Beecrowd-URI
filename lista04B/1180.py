a = int(input())
vetor = []
string = input().split()
o = string[0]
for i in range(a):
    if int(string[i]) < int(o):
        o = string[i]
        a = i
print(f'Menor valor: {o}')
print(f'Posicao: {a}')