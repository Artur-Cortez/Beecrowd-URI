andar1 = int(input())
andar2 = int(input())
andar3 = int(input())

tempo1 = andar2 * 2 + andar3 * 4
tempo2 = andar1 * 2 + andar3 * 2
tempo3 = andar1 * 4 + andar2 * 2

lista = [tempo1, tempo2, tempo3]
lista.sort()
print(lista[0])