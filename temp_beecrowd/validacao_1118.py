validos = 0
lista = []
terminou = False
loop_grande = True

while loop_grande:
  while validos != 2:
    entrada = float(input())
    if entrada > 0 and entrada <= 10:
      lista.append(entrada)
      validos += 1
    else: print('nota invalida')  
  print(f'media = {((sum(lista))/2):.2f}')
  
  terminou = True
  while terminou:
    print('novo calculo (1-sim 2-nao)')
    a = int(input())
    if a == 1: 
      validos, lista = 0, []
      terminou = False
    elif a == 2: 
      loop_grande = False
      terminou = False
  