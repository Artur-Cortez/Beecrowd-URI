pares, impares = 0, 0
print('Digite quatro valores inteiros')
for i in range(4):
    entrada = int(input())
    if entrada % 2 == 0:
        pares += entrada
    else: impares += entrada

print()
print('Soma dos pares = ', pares)
print('Soma dos ímpares = ', impares)
