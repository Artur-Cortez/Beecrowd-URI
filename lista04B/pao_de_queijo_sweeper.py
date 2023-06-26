while True:
  try:    
    linhas, colunas = map(int, input('linhas e colunas').split())
    matriz = []
    linha = [0] * (colunas+2)
    matriz.append(linha)
    for i in range(linhas):
      a = list(map(int, input().split()))
      a.insert(0, 0)
      a.append(0)
      matriz.append(a)
      linha2 = [0] * (colunas+2)
      matriz.append(linha2)
    
    resultado = []
    
    for k in range(linhas+2):
      resultado.append(linha)
    
    #percorre as linhas
    for l in range(1, linhas + 1):
      #percorre as colunas
      for c in range(1, colunas + 1):
        if matriz[l][c] == 1:
          resultado[l][c] = 9
        else:   
          resultado[l][c] = matriz[l-1][c] + matriz[l+1][c] + matriz[l][c-1] + matriz[l][c+1]
    
    for l in range(1, linhas + 1):
      #percorre as colunas
      for c in range(1, colunas + 1):
        print(resultado[l][c], end="")
      print()
      
  except EOFError:
    break


#     #Código para fazer o append para a nova matriz
#     nova_matriz.append(adjacentes)
  
# print(nova_matriz)