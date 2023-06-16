class Pais:
  def __init__(self, nome, populacao, area):
    self.__nome, self.__populacao, self.__area = '', 0, 0
    self.set_nome(nome)
    self.set_populacao(populacao)
    self.set_area(area)
  
  def set_nome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()

  def set_populacao(self, populacao):
    if populacao >= 0: self.__populacao = populacao
    else: raise ValueError()
    
  def set_area(self, area):
    self.__area = area

  def get_nome(self):
    return self.__nome
    
  def get_populacao(self):
    return self.__populacao
    
  def get_area(self):
    return self.__area

  def densidade(self):
    return self.__populacao / self.__area

  def __str__(self):
    return print(f"\nNome: {self.__nome}\nPopulação: {self.__populacao}\nÁrea: {self.__area}\nDensidade demográfica: {self.densidade()} hab/km²")


class UI:
  def main():
    lista = []
    for i in range(2):
      print(f'País {i+1}')
      nome = input(f'Nome do {i+1}º país: ')
      populacao = int(input(f'População do {i+1}º país: '))
      area = float(input(f'Área do {i+1}º país: '))
      
      x = Pais(nome, populacao, area)
      lista.append(x)
      
    maior_densidade = 0
    posicao = 0
    
    for j in range(len(lista)):
      if lista[j].densidade() > maior_densidade:
        maior_densidade = lista[j].densidade()
        posicao = j
        
    print(lista[posicao].__str__())

UI.main()