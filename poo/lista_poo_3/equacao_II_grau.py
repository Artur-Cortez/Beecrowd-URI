class EquacaoIIgrau:

  def __init__(self, a, b, c):
    self.__a, self.__b, self.__c = 999, 999, 999
    self.set_a(a)
    self.set_b(b)
    self.set_c(c)

  def set_a(self, a):
    if a != 0: self.__a = a
    else: raise ValueError()

  def set_b(self, b):
    self.__b = b

  def set_c(self, c):
    self.__c = c

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b

  def get_c(self):
    return self.__c

  def delta(self):
    return self.__b**2 - 4 * self.__a * self.__c

  def temraizesreais(self):
    if self.delta() >= 0: return True
    else: return False

  def raiz1(self):
    if self.temraizesreais():
      raiz1 = (-self.__b + self.delta()**0.5) / 2 * self.__a
    else:
      raiz1 = 'Não real'
    return raiz1
    
  def raiz2(self):
    if self.temraizesreais():
      raiz2 = (-self.__b - self.delta()**0.5) / 2 * self.__a
    else:
      raiz2 = 'Não real'
    return raiz2

  def __str__(self):
    return f'''\nEquação: {self.__a}x² + {self.__b}x + {self.__c}, A = {self.__a}, B = {self.__b}, C = {self.__c}
Delta = {self.delta()}
Tem raízes reais: {self.temraizesreais()}, Raíz 1 = {self.raiz1()}, Raíz 2 = {self.raiz2()}
    '''


class UI:

  def main():
    print('Informe os coeficientes A, B e C')
    x = EquacaoIIgrau(int(input()), int(input()), int(input()))

    print(x)


UI.main()
