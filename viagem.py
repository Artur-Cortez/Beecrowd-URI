class Viagem:

  def __init__(self):
    self.__distancia = 0
    self.__tempo = ''

  def set_distancia(self, distancia):
    if distancia > 0: self.__distancia = distancia
    else: raise ValueError()

  def set_tempo(self, tempo):
    if tempo >= 0: self.__tempo = tempo
    else: raise ValueError()

  def get_distancia(self):
    return self.__distancia

  def get_tempo(self):
    return self.__tempo

  def calc_velocidade_media(self):
    return self.__distancia / self.__tempo


class UI:

  @staticmethod
  def main():
    x = Viagem()

    nome = int(input('Informe a distância percorrida: '))
    x.set_distancia(nome)

    tempo = input('Informe o tempo gasto: ')
    horas, minutos = map(int, tempo.split(':'))
    x.set_tempo(tempo)
    print(f"{x.get_distancia()} km")
    print(f"{x.get_tempo()} h")
    print(f"{x.get_distancia()} km/h")

    x.calc_velocidade_media()


UI.main()
