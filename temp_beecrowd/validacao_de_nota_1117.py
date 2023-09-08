validos = 0
lista = []
while validos != 2:
  entrada = float(input())
  if entrada > 0 and entrada <= 10:
    lista.append(entrada)
    validos += 1
  else: print('nota invalida')

print(f'media = {((sum(lista))/2):.2f}')