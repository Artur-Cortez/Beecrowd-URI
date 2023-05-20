class PecaDomino:

  def __init__(self, ponta_x0, ponta_y0):
    self.__pontax, self.__pontay = 0, 0
    self.set_pontax(ponta_x0)
    self.set_pontay(ponta_y0)

  def set_pontax(self, ponta_x):
    if type(ponta_x) == int and ponta_x >= 1 and ponta_x <= 6:
      self.__pontax = ponta_x

  def set_pontay(self, ponta_y):
    if type(ponta_y) == int and ponta_y >= 0 and ponta_y <= 6:
      self.__pontay = ponta_y

  def get_pontax(self):
    return self.__pontax

  def get_pontay(self):
    return self.__pontay

  def combinar(self, peca):
    if self.get_pontax() == peca.get_pontax() or self.get_pontax() == peca.get_pontay() or self.get_pontay() == peca.get_pontax() or self.get_pontay() == peca.get_pontay():
      return True
    else:
      return False
  def __str__(self):
    return print(f'A 1a cabeça é {self.__pontax} e a 2a cabeça é {self.__pontay}')


class UI:

  def main():
    ponta_x1, ponta_y1, = map(
      int,
      input('Informe a 1a peça (ex: 6|6, 3|5...): ').split('|'))
    peca1 = PecaDomino(ponta_x1, ponta_y1)
    print(peca1.__str__())
    
    ponta_x2, ponta_y2, = map(
      int,
      input('Informe a 2a peça (ex: 6|6, 3|5...): ').split('|'))
    peca2 = PecaDomino(ponta_x2, ponta_y2)
    print(peca2.__str__())

    if peca1.combinar(peca2) == True:
      print("As peças podem combinar")
    else: print("As peças não podem combinar")


UI.main()