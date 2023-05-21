class Viagem:

  def __init__(self, distancia, tempo):
    self.__distancia, self.__tempo = 0, ''
    self.set_distancia(distancia)
    self.set_tempo(tempo)

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

    distancia = float(input('Informe a distância percorrida: '))
    tempo = input('Informe o tempo gasto: ')
    horas, minutos = map(int, tempo.split(':'))
    tempo = horas + minutos/60
    x = Viagem(distancia, tempo)
    print(f"{x.get_distancia()} km")
    print(f"{x.get_tempo()} h")
    print(f"{x.get_distancia()} km/h")

UI.main()
