class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return print(f'Área do círculo: {3.14*self.raio**0.5}')

    def calcular_circunferência(self):
        return print(f'Circunferência do círculo: {3.14*2*self.raio}')


bola = Circulo(5)

bola.calcular_area()

bola.calcular_circunferência()