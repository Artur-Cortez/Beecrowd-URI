import json, datetime

class Livro:
  def _init__(self, id, titulo, autor, ano, data_de_devolucao):
    self.__titulo, self.__autor = titulo, autor
    self.__ano, self.__data_de_devolucao = ano, data_de_devolucao

  def set_id(self, id): self.__id = id
  def get_id(self): return self.__id

  def set_titulo(self, titulo): self.__titulo = titulo
  def get_titulo(self): return self.__titulo
  
  def set_autor(self, autor): self.__autor = autor
  def get_autor(self): return self.__autor

  def set_ano(self, ano): self.__ano = ano
  def get_ano(self): return self.__ano

  def set_data_de_devolucao(self, data_de_devolução):
    self.__data_de_devolucao = data_de_devolução
  def get_data_de_devolucao(self):
    return self.__data_de_devolucao

  def __str__(self):
    return f'ID: {self.__id}\nTítulo: {self.__titulo}\naAutor: {self.__autor}\nAno: {self.__ano}\nData de devolução: {self.__data_de_devolucao}'


class NLivro:
  __livros = []

  @classmethod
  def inserir(cls, l): 
    id = 0

    for livro in cls.__livros:
      if livro.get_id() > id: id = livro.get_id()
    l.set_id(id+1)

    cls.__livros.append(l)

  @classmethod
  def listar(cls): return cls.__livros

  def listar_id(cls, id):
    for obj in cls.__livros:
      if obj.get_id() == id:
        return obj
        
  @classmethod 
  def atualizar(cls, id, titulo='', autor='', ano='', data_de_devolucao=''):
    l = cls.listar_id(id)

    if titulo == '': pass
    else: l.set_titulo(titulo)

    if autor == '': pass
    else: l.set_autor(autor)

    if ano == '': pass
    else: l.set_ano(ano)

    if data_de_devolucao == '': pass
    else: l.set_data_de_devolucao(data_de_devolucao)

  def excluir(cls, id):
    l = cls.listar_id(id)
    cls.__livros.remove(l)

  def salvar(cls):
    with open("Rev_prova/lista_biblioteca.json") as arquivo:
      json.dump(cls.__livros, arquivo, indent=4, default=vars)

  def abrir(cls):
    cls.__livros = []

    with open("Rev_prova/lista_biblioteca.json") as arquivo:
      livros = json.load(arquivo)

      for obj in livros:
        l = Livro(obj["_Livro__id"], obj["_Livro__titulo"], obj["_Livro__autor"], obj["_Livro__ano"], obj["_Livro_data_de_devolucao"])
        cls.__livros.append(l)



class UI:
  def main():
    op = 0
    while op != 99:
      pass

  def menu():
    print("\n1 - Inserir Livro, 2 - Listar")