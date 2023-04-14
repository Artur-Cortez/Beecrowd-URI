maior = 0
posicao = 0
for i in range(1, 101):
  entrada = int(input())
  if entrada > maior:
    maior = entrada
    posicao = i
print(maior)
print(posicao)