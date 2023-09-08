import datetime

class Local:
  def __init__(self, id, nome, endereco):
    self.__id, self.__nome = id, nome
    self.__endereco = endereco
    
class Evento:
  def __init__(self, id, nome, data_hora):
    self.__id, self.__nome = id, nome
    self.__data_hora = data_hora
    
class Personagem:
  def __init__(self, id, nome, id_evento, id_artista):
    self.__id, self.__nome = id, nome
    self.__id_evento, self.__id_artista = id_evento, id_artista    
    
class Artista:
  def __init__(self, id, nome):
    self.__id, self.__nome = id, nome
    
class Curtida:
  def __init__(self, id, nome, id_evento, id_usuario):
    self.__id, self.__nome = id, nome
    self.__id_evento, self.__id_usuario = id_evento, id_usuario
    
class Comentário:
  def __init__(self, id, nome, id_evento, id_usuario):
    self.__id, self.__nome = id, nome
    self.__id_evento, self.__id_usuario = id_evento, id_usuario
    
class Usuário:
  def __init__(self, id, nome, email):
    self.__id, self.__nome = id, nome
    self.__email = email

class crud_:
  def __init__(self):
    self.locais = []

  def inserir()
  