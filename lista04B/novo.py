entrada = int(input())
cont = entrada
lista = []
lista.append(entrada)
for i in range(9):
  lista.append(cont*2)
  cont += lista[i]  

for j in range(10):  
  print(f'N[{j}] = {lista[j]}')