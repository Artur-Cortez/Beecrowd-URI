import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id, self.__nome, self.__email, self.__fone = id, nome, email, fone

  def set_id(self, id): self.__id = id
  def get_id(self):  return self.__id
  def set_nome(self, nome): self.__nome == nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone

  def __str__(self):
    return f'\nID: {self.__id}\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__fone}'

class NCliente: 
  __clientes = [] #lista de dicionarios

  @classmethod
  def inserir(cls, c):
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id:  id = cliente.get_id()
        
    c.set_id(id+1)
   
    cls.__clientes.append(c)    
    
  @classmethod
  def listar_id(cls, id):
    for i in cls.__clientes:
      if i.get_id() == id:
        return i
        
  @classmethod
  def listar(cls):
    return cls.__clientes
      
  @classmethod
  def atualizar(cls, id, nome='', email='', fone=''):
    c = cls.listar_id(id)
    
    if nome == '': pass      
    else: 
      c.set_nome(nome)
      
    if email == '': pass
    else:
      c.set_email(email)
      
    if fone == '': pass
    else:
      c.set_fone(fone)

  @classmethod        
  def excluir(cls, id):
    c = cls.listar_id(id)
    cls.__clientes.remove(c)
    
  @classmethod
  def abrir(cls):
   with open("list_rev_07_crud/lista.json", "r") as arquivo:
     clientes_json = json.load(arquivo)
     for obj in clientes_json:
       c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
       cls.__clientes.append(c)

  @classmethod
  def salvar(cls):
     with open("list_rev_07_crud/lista.json", "w") as arquivo:
       json.dump(cls.__clientes, arquivo, indent=4, default = vars)

class UI:
  @classmethod
  def Main(cls):
    op = 0
    while op != 99:
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
      if op == 5: UI.ClienteSalvar()
      if op == 6: UI.ClienteAbrir()

  @classmethod
  def Menu(cls):
    print("\n1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Salvar, 6 - Abrir, 99 - sair\n")
    return (int(input(">> ")))
    
  @classmethod
  def ClienteInserir(cls):    
    nome = input("\nNome: ")
    email = input("Email: ")
    fone = input("Telefone: ")
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
    NCliente.salvar()
  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar(): print(cliente)

  @classmethod
  def ClienteAtualizar(cls):
    cls.ClienteListar()
    id = int(input("\nInsira o id: "))
    nome = input("Nome: ")
    email = input("Email: ")
    fone = input("Telefone: ")    
    NCliente.atualizar(id, nome, email, fone)
    NCliente.salvar()
    
  @classmethod
  def ClienteExcluir(cls):
    id = int(input("insira o id: "))
    NCliente.excluir(id)
    NCliente.salvar()
    

  @classmethod
  def ClienteSalvar(cls):
    NCliente.salvar()
    
  @classmethod
  def ClienteAbrir(cls):
    NCliente.abrir()

UI.Main()
