from random import choice


class Bingo:

  def __init__(self, p_numBolas, p_lista_principal, p_lista_sorteados):
    self.lista_principal = p_lista_principal
    self.lista_sorteados = p_lista_sorteados
    self.__comecou = False
    self.__numBolas = 0
    self.iniciar(p_numBolas)

  def iniciar(self, numBolas):
    try:
      if numBolas >= 2: 
        self.__numBolas = numBolas
        for i in range(1, self.__numBolas+1):
          self.lista_principal.append(i)
        
      else: raise ValueError('Erro: O valor desse ser maior igual a 2')
        
    except ValueError as error:
      print(error)

  def get_numBolas(self):
    return self.__numBolas

  def proximo(self):
    
    if len(self.lista_principal) == 0 and self.__comecou == True: print(-1)
    else:
      bola = choice(self.lista_principal)
      self.lista_sorteados.append(bola)
      self.lista_principal.remove(bola)
      self.__comecou = True
      print(f'Bola sorteada: {bola}\n')

  def sorteados(self):
    print(f'Bolas sorteadas: {self.lista_sorteados}\n')


class UI:

  def main():
    lista_principal, lista_sorteados = [], []

    novo_bingo = Bingo(int(input('quantas bolas: ')), lista_principal, lista_sorteados)

    while True:
      print('Insira a tecla desejada: ')
      print('P - Sorteia a próxima bola')
      print('S - Mostra as bolas sorteadas até o momento')
      print('E - Encerrar o programa')
      print()

      entrada = input().lower()
      if entrada == 'p': novo_bingo.proximo()
      elif entrada == 's': novo_bingo.sorteados()
      elif entrada == 'e': break


UI.main()
