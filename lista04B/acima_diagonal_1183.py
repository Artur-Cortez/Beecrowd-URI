matriz = []
entrada = input()
for i in range(12):
  linha = []
  for j in range(12):
    valor = float(input())
    linha.append(valor)
  matriz.append(linha)

if entrada == 'S':
  soma = 0
  for a in range(12):
    for b in range(12):
      if b > a:
        soma += matriz[a][b]
  print(f'{soma:.1f}')

elif entrada == 'M':
  sub_lista = []
  for a in range(12):
    for b in range(12):
      if b > a:
        sub_lista.append(matriz[a][b])
  print(f'{(sum(sub_lista)/len(sub_lista)):.1f}')
