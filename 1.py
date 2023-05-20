class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def set_raio(self, raio):
        if raio > 0: self.__raio = raio
        else: raise ValueError()

    def get_raio(self):
        return self.__raio    

    def calcular_area(self):
        return print(f'Área do círculo: {3.14*self.__raio**0.5}')

    def calcular_circunferência(self):
        return print(f'Circunferência do círculo: {3.14*2*self.__raio}')



class UI:
  def main():
    print()