class Disciplina:

  def __init__(self):
    self.__disciplina = ''
    self.__n1, self.__n2, self.__n3, self.__n4, self.__npfinal = 0, 0, 0, 0, 0

  def set_disciplina(self, nome_da_disciplina):
    disciplinas = [
      'Sociologia', 'Arte', 'Filosofia', 'Matemática', 'Física', 'Geografia',
      'PEOO', 'LPL', 'Educação Física', 'Química',
      'Design web e Arquitetura da informação'
    ]
    if nome_da_disciplina in disciplinas and nome_da_disciplina != '':
      self.__disciplina = nome_da_disciplina
    else:
      raise ValueError()

  def set_n1(self, n1):
    if n1 >= 0 and n1 <= 100: self.__n1 = n1
    else: raise ValueError()

  def set_n2(self, n2):
    if n2 >= 0 and n2 <= 100: self.__n2 = n2
    else: raise ValueError()

  def set_n3(self, n3):
    if n3 >= 0 and n3 <= 100: self.__n3 = n3
    else: raise ValueError()

  def set_n4(self, n4):
    if n4 >= 0 and n4 <= 100: self.__n4 = n4
    else: raise ValueError()

  def set_npfinal(self, npfinal):
    if npfinal >= 0 and npfinal <= 100: self.__npfinal = npfinal
    else: raise ValueError()

  def get_disciplina(self):
    return self.__disciplina

  def get_n1(self):
    return self.__n1

  def get_n2(self):
    return self.__n2

  def get_n3(self):
    return self.__n3

  def get_n4(self):
    return self.__n4
    
  def get_npfinal(self):
    return self.__npfinal

  def calc_media_parcial(self):
    return (self.__n1 * 2 + self.__n2 * 2 + self.__n3 * 3 + self.__n4 * 3) / 10

  def calc_media_final(self):
    media_parcial = self.calc_media_parcial()
    if media_parcial >= 60:
        return media_parcial
    else:
        return (media_parcial + self.__npfinal) / 2 

  def __str__(self):
    return f'Disciplina: {self.get_disciplina()}\nMédia Parcial: {self.calc_media_parcial()}\nMédia Final: {self.calc_media_final()}'



class UI:

  @staticmethod
  def main():
    print('----------------------\nSUAP\n----------------------\n')

    x = Disciplina()
    disciplina = input('Informe o nome da disciplina: ')
    x.set_disciplina(disciplina)

    n1 = int(input('Informe a nota do 1º bimestre: '))
    x.set_n1(n1)
    n2 = int(input('Informe a nota do 2º bimestre: '))
    x.set_n2(n2)
    n3 = int(input('Informe a nota do 3º bimestre: '))
    x.set_n3(n3)
    n4 = int(input('Informe a nota do 4º bimestre: '))
    x.set_n4(n4)

    pfinal = input('Realizou prova final? (S/N): ')
    if pfinal == 'S':
      npfinal = int(input('Informe a nota da prova final: '))
      x.set_npfinal(npfinal)

    print(x)


UI.main()
