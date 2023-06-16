class Frete:
  def __init__(self, distancia, peso):
    self.__distancia, self.__peso = 0, 0
    self.set_distancia(distancia)
    self.set_peso(peso)

  def set_distancia(self, distancia):
    if distancia >= 0: self.__distancia = distancia
    else: raise ValueError()

  def set_peso(self, peso):
    if peso >= 0: self.__peso = peso
    else: raise ValueError()

  def get_distancia(self):
    return self.__distancia

  def get_peso(self):
    return self.__peso

  def calc_frete(self):
    return self.__distancia * self.__peso * 0.01

  def __str__(self):
    return f'Distância: {self.__distancia}km Peso: {self.__peso}kg\nValor do frete: {self.calc_frete()}'

class UI:
  def main():
    print('Insira a distância e o peso')
    x = Frete(float(input()), float(input()))
    print(x)
    

UI.main()