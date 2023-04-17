lista, media = [], 0
print('Digite quatro valores inteiros')

for i in range(4):
    valor = int(input())
    media += valor
    lista.append(valor)
media /= 4

print(f'Média = {media}')
print('Números menores que a média')
menores = [x for x in lista if x < media]
for z in menores:
    print(z)

print('Números maiores que a média')  
maiores = [x for x in lista if x >= media]
for z in maiores:
    print(z)