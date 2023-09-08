import datetime

# self é uma palavra-chave para se referir a coisas do proprio objeto

# construtor 

class Amigo:
  
  def __init__(self, nome, nasc):
    
    self.__nome, self.__nasc = '', ''

    # self.set_nome(nome)
    # self.set_nasc(nasc)

  def set_nome(self, nome):
    try:
      if nome.strip() != '':
        self.__nome = nome
      else: raise ValueError('Nome não pode ser vazio')
    except ValueError: print(ValueError)

  def set_nasc(self, nasc):
    dia, mes, ano = map(int, nasc.split('/'))
    self.__nasc = datetime.datetime(ano, mes, dia)

  def get_nome(self):
    return self.__nome
  
  def get_nasc(self):
     return self.__nasc

  def __str__(self):
    return f'Nome: {self.__nome}\nData de nascimento: {self.__nasc}'

class UI:
  def main():
    idade_do_mais_novo = datetime.datetime(1800, 10, 10)
    amigo_mais_novo = 0

    ncasos = int(input('Quantos amigos:'))
    
    for i in range(ncasos):
      amigo = Amigo(input('Nome do amigo: '), input('Nasc (xx/xx/xxxx): '))

      if amigo.get_nasc() > idade_do_mais_novo:
        amigo_mais_novo = amigo        
        idade_do_mais_novo = amigo.get_nasc()
      
    print(f'O amigo mais novo é {amigo_mais_novo.get_nome()} e a idade dele é {idade_do_mais_novo.strftime("%d/%m/%Y")}')

UI.main()
    