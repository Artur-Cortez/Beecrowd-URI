n = int(input())
lista = []
lista_sem_repetidos = []
for _ in range(n):
    entrada = int(input())
    lista.append(entrada)

lista_sem_repetidos = list(set(lista))

for j in lista_sem_repetidos:
    count = lista.count(j)
    print(f"{j} aparece {count} vez(es)")
