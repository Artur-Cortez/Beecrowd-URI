def ordena(matriz):
  i = 1
  while i < 10:
    j = i - 1          # elemento anterior
    pivo = matriz[i]   # elemento atual como [0.23, 1]

    # valor de oleosidade do elemento anterior < oleosidade do atual ?
    while j >= 0 and matriz[j][0] < pivo[0]:      
      matriz[j+1] = matriz[j]
      j -= 1
      
    matriz[j + 1] = pivo
    i += 1
    
qtcasos = 0
matriz = []
while True:
  try:
    
    n_digitos = int(input())
    
    valores = input().split()

    for i in range(10):
      sublista = [float(valores[i]), i]
      matriz.append(sublista)
      
    ordena(matriz)
    qtcasos += 1
    print(f"Caso {qtcasos}: ", end="")
    for k in range(n_digitos):
      print(matriz[k][1], end="")

    print()
    matriz = []
  
  except EOFError: break