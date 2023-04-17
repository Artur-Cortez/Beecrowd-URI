lista, pares, impares = [], 0, 0
print('Digite quatro valores inteiros')
for i in range(4):
    valor = int(input())
    if valor %2 == 0:
        pares += valor
    else: impares += valor
print(f'Soma dos pares = {pares}')
print(f'Soma dos ímpares = {impares}')
