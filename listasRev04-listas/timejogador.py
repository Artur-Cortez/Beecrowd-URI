class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome, self.__camisa, self.__gols = '', '', 0
    self.set_nome(nome)
    self.set_camisa(camisa)
    self.set_gols(gols)

  def set_nome(self, nome):
    try:
      if nome.strip() != '':
        self.__nome = nome
      else: raise ValueError('Nome não pode ser vazio')
    except ValueError: print(ValueError)

  def set_camisa(self, camisa):
    self.__camisa = camisa

  def set_gols(self, gols):
    try:
      if gols >= 0:
        self.__gols = gols
      else: raise ValueError('Nº de gols n pode ser negativo')
    except ValueError: print(ValueError)

  def get_nome(self):
    return self.__nome
  
  def get_gols(self):
    return self.__gols

class Time:
  def __init__(self, nome, estado):
    self.__nome, self.__estado, self.__jogadores = '', '', []
    

  def set_nome(self, nome): #   "joaogomes"
    try:
      if nome.strip() != '':
        self.__nome = nome
      else: raise ValueError('Nome não pode ser vazio')
    except ValueError: print(ValueError)

  def set_estado(self, estado):
    try:
      if estado.strip() != '':
        self.__estado = estado
      else: raise ValueError('Nome do estado não pode ser vazio')
    except ValueError: print(ValueError)

  def inserir(self, jogador):
    self.__jogadores.append(jogador)

  def listar(self):
    return self.__jogadores
  
  def artilheiro(self):
    artilheiro = self.__jogadores[0]
    for i in self.__jogadores:
      if i.get_gols() > artilheiro.get_gols():

        artilheiro = i
    return artilheiro

  def __str__(self):
    return f' Time: {self.__nome}\n Estado: {self.__estado}'

class UI: 
  def main():
    time = Time('gls', 'RN')
    comando = '''Comandos:
-----------------------------
--> 2 - adcionar_jogador
--> 3 - listar_jogadores (time)
--> 4 - artilheiro
-----------------------------
    '''
    print(comando)

    while True:
      entrada = int(input('--> '))

      if entrada == 2:
        novo_jogador = Jogador(input('Nome: '), input)