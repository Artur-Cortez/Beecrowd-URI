linhas, colunas = map(int, input('linhas e colunas').split())
matriz = []
linha = [0] * (colunas+2)
matriz.append(linha)
for i in range(linhas):
  a = list(map(int, input().split()))
  a.insert(0, 0)
  a.append(0)
  matriz.append(a)
linha = [0] * (colunas+2)
matriz.append(linha)
print(matriz)


# matriz_teste = [[0, 0, 0, 0, 0, 0][0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0],
#                 [0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0]]

# nova_matriz = []

# #percorre as linhas
# for i in range(linhas + 1):
#   #percorre as colunas
#   for j in range(colunas - 2):
#     adjacentes = 0

#     #se não tiver pão de queijo
#     if matriz_teste[i][j] == 0:
#       #À esquerda
#       if matriz_teste[i][j - 1] == 1: adjacentes += 1
#       #Em cima
#       if matriz_teste[i - 1][j] == 1: adjacentes += 1
#       #À esquerda
#       if matriz_teste[i][j + 1] == 1: adjacentes += 1
#       #Em baixo
#       if matriz_teste[i + 1][j] == 1: adjacentes += 1
#     else: adjacentes = 9

#     #Código para fazer o append para a nova matriz
#     nova_matriz.append(adjacentes)
  
# print(nova_matriz)