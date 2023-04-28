soma = 0
lista = []
print('Digite quatro valores inteiros')
for i in range(4):
    entrada = int(input())
    soma += entrada
    lista.append(entrada)

media = (soma)/4
print("Média = ", media)
print("Números menores que a média")
for i in lista:
    if i < media:
        print(i)
print("Números maiores ou iguais à média")
for i in lista:
    if i >= media:
        print(i)