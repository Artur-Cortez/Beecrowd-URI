
lista_de_somas = []
num_jogadores, num_rodadas = map(int, input().split())
valores = input().split()

for i in range(num_jogadores):
  inicio = i
  var = 0
  for j in range(inicio, len(valores), num_jogadores):
    var += int(valores[j])
  lista_de_somas.append(var)

jogador_com_maior_pontuacao = 1

maior_pontuacao = max(lista_de_somas)

for i in range(len(lista_de_somas)):
  if lista_de_somas[i] == maior_pontuacao:
    jogador_com_maior_pontuacao = i+1
  
print(jogador_com_maior_pontuacao)

