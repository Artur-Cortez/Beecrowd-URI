class Usuario:
  def __init__(self, id, nome, email):
    self.__id, self.__nome, self.__email = id, nome, email

class NUsuario:
  def __init__(self):
    self.__usuarios = []
  def inserir(self, u):
    self.__usuarios.append(u)
  def listar(self): return self.__usuarios

class UI:

  def main(self):
    op = 10
    while op != 0:
      op = self.menu()
      if op == 1: self.inserir_usuario()
  
  @staticmethod
  def menu(self):
    print("0 -  bla, 1 - bla, 2 - lbla")

    return int(input())

  @staticmethod

UI.main()