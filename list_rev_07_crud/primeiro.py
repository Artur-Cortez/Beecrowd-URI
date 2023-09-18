
import json, datetime

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

class Horario: 
  def __init__(self, id, data, confirmado, idCliente, idServico):
    self.__id, self.__data = id, data
    self.__confirmado, self.__idCliente = confirmado, idCliente
    self.__idServico = idServico

  def set_id(self, id):
    self.__id = id
    
  def get_id(self):
    return self.__id

  def set_data(self, data):
    self.__data = data
  
  def get_data(self):
    return self.__data
  
  def set_confirmado(self, status_de_confirmacao):
    self.__confirmado = status_de_confirmacao

  def get_confirmado(self): return self.__confirmado

  def set_idCliente(self, idCliente):
    self.__idCliente = idCliente

  def get_idCliente(self): return self.__idCliente

  def get_idServico(self): return self.__idServico

  def set_idServico(self, idServico):
    self.__idServico = idServico

  def __str__(self):
    return f'ID do horário: {self.__id}\nData: {self.__data}\nConfirmado: {self.__confirmado}\nID do cliente: {self.__idCliente}\nID do serviço: {self.__idServico}\n'

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id, self.__descricao = id, descricao
    self.__valor, self.__duracao = valor, duracao #duracao é do tipo int

  def set_id(self, id): self.__id = id
  def get_id(self): return self.__id
  
  def set_descricao(self, descricao):
    self.__descricao = descricao

  def set_valor(self, valor):
    self.__valor = valor

  def set_duracao(self, duracao):
    self.__duracao = duracao

  def __str__(this):
    return f'ID: {this.__id}\nDescrição: {this.__descricao}\nValor: {this.__valor}\nDuração: {this.__duracao}'

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
    print('-----LISTA CLIENTES-----\n')
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
  def salvar(cls):
     with open("list_rev_07_crud/lista_clientes.json", "w") as arquivo:
       
       json.dump(cls.__clientes, arquivo, indent=4, default = vars)

  @classmethod
  def abrir(cls):
    cls.__clientes = []
    with open("list_rev_07_crud/lista_clientes.json", "r") as arquivo:
     clientes_json = json.load(arquivo)
     for obj in clientes_json:
       c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
       cls.__clientes.append(c)
      
class NHorario:
  __horarios = []

  @classmethod
  def inserir(cls, hor):
    
    id = 0
    for horario in cls.__horarios:
      if horario.get_id() > id:  id = horario.get_id()
        
    hor.set_id(id+1)
   
    cls.__horarios.append(hor)

  @classmethod
  def listar(cls): return cls.__horarios

  @classmethod
  def listar_id(cls, id):
    for i in cls.listar():
      if i.get_id() == id:
        return i

  @classmethod
  def atualizar(cls, id, data, confirmado, idCliente, idServico):
    h = cls.listar_id(id)

    h.set_data(data)

    h.set_confirmado(confirmado)
    h.set_idCliente(idCliente)
    h.set_idServico(idServico)
  
    
  @classmethod        
  def excluir(cls, id):
    h = cls.listar_id(id)
    cls.__horarios.remove(h)

  @classmethod
  def salvar(cls):
    with open("list_rev_07_crud/lista_horarios.json", "w") as arquivo:

        for horario in cls.__horarios:
            horario.set_data(horario.get_data().strftime('%Y-%m-%d %H:%M:%S'))

        json.dump(cls.__horarios, arquivo, indent=4, default=vars)  

  @classmethod
  def abrir(cls):
    cls.__horarios = []
    with open("list_rev_07_crud/lista_horarios.json", "r") as arquivo:
     horarios_json = json.load(arquivo)
     for obj in horarios_json:

       data_formatada = datetime.datetime.strptime(obj["_Horario__data"], '%Y-%m-%d %H:%M:%S')
       
       h = Horario(obj["_Horario__id"], data_formatada, obj["_Horario__confirmado"], obj["_Horario__idCliente"], obj["_Horario__idServico"])
       cls.__horarios.append(h)


class NServico:
  __servicos = []

  @classmethod
  def inserir(cls, s):
    
    id = 0
    for servico in cls.__servicos:
      if servico.get_id() > id:  id = servico.get_id()
        
    s.set_id(id+1)
   
    cls.__servicos.append(s)

  @classmethod
  def listar_id(cls, id):
    for i in cls.__servicos:
      if i.get_id() == id:
        return i
        
  @classmethod
  def listar(cls):
    print('-----LISTA SERVIÇOS-----\n')
    return cls.__servicos

  @classmethod
  def atualizar(cls, id, descricao, valor, duracao):
    s = cls.listar_id(id)
    
    s.set_descricao(descricao)
    s.set_valor(valor)
    s.set_duracao(duracao)
  
  @classmethod
  def abrir(cls):
    cls.__servicos = []
    with open("list_rev_07_crud/lista_servicos.json", "r") as arquivo:
     
     horarios_json = json.load(arquivo)
     
     for obj in horarios_json:
       s = Servico(obj["_Servico__id"], obj["_Servico__descricao"], obj["_Servico__valor"], obj["_Servico__duracao"] )
       cls.__servicos.append(s)

  @classmethod
  def salvar(cls):
     with open("list_rev_07_crud/lista_servicos.json", "w") as arquivo:
       json.dump(cls.__servicos, arquivo, indent=4, default = vars)

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

      if op == 5: UI.ServicoInserir()
      if op == 6: UI.ServicoListar()
      if op == 7: UI.ServicoAtualizar()
      if op == 8: UI.ServicoExcluir()

      if op == 9: UI.HorarioInserir()
      if op == 10: UI.HorarioAtualizar()
      if op == 11: UI.HorarioExcluir()
      if op == 12: UI.HorariosCriar()
      if op == 13: UI.HorarioListar()

  @classmethod
  def Menu(cls):
    print("\n1 - Ins_cli, 2 - List_cli, 3 - Atuali_cli, 4 - Del_cli\n\n5 - Ins_serv, 6 - List_serv, 7 - Atuali_serv, 8 - Del_serv\n\n9 - Inserir_horario, 10 - Atualizar_horario, 11 - Cancelar_horario\n\n12 - Criar os horários, 13 - Lista horarios, 99 - sair\n")
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
    cls.ClienteAbrir()
    for cliente in NCliente.listar(): print(cliente)

  @classmethod
  def ClienteAbrir(cls):
    NCliente.abrir()

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
  def ServicoInserir(cls):
    cls.ServicoAbrir()
    desc = input("Descrição do serv.: ")
    valor = float(input("Valor do serv.: "))
    duracao = input("Duracao do serv.: ")

    servico = Servico(0, desc, valor, duracao)
    NServico.inserir(servico)
    NServico.salvar()
  
  @classmethod
  def ServicoAtualizar(cls):
    cls.ServicoListar()
    id = int(input('\nInsira o id: '))
    desc = input('Nova desc: ')
    valor = float(input('Novo valor: '))
    duracao = input('Nova duracao: ')

    NServico.atualizar(id, desc, valor, duracao)
    NServico.salvar()

  @classmethod
  def ServicoAbrir(cls):
    NServico.abrir()
    
  @classmethod
  def ServicoListar(cls):
    cls.ServicoAbrir()
    for servico in NServico.listar(): print(servico)

  @classmethod
  def ServicoExcluir(cls):
    id = int(input("Insira o id: "))
    NServico.excluir(id)
    NServico.salvar()

  @classmethod
  def HorarioAbrir(cls):
    NHorario.abrir()

  @classmethod
  def HorarioListar(cls):
    cls.HorarioAbrir()
    for horario in NHorario.listar(): 
      print(horario)
  
  @classmethod
  def HorarioInserir(cls):
    cls.HorarioAbrir()
    
    print('\n-----Horários disponíveis-----\n')
    for horario in NHorario.listar():
      if not horario.get_confirmado():
        aux = horario.get_data().hour

        print(f'ID: {horario.get_id()}')
        print(f'Horário: {aux}h - {aux+1}h\n')
      
    id_hor = int(input('Insira o id do horário: '))
    print('-----Serviços disponíveis-----')
    cls.ServicoListar()
    id_serv = int(input('Insira o id do serv: '))
    
    cls.ClienteListar()
    id_cli = int(input('Insira o id do cli: '))
    
    hor_escolhido = NHorario.listar_id(id_hor)
    
    hor_escolhido.set_idCliente(id_cli)
    hor_escolhido.set_idServico(id_serv)
    hor_escolhido.set_confirmado(True)
    NHorario.salvar()


  @classmethod
  def HorarioAtualizar(cls):
    cls.HorarioAbrir()

    cls.HorarioListar()
    id_hor = int(input('Insira o id do horário: '))

    n_data = datetime.datetime.strptime(input('Insira a nova data'), '%d/%m/%Y %H:%M')
    confirmado = input('Confirmação digite S ou N: ')
    if confirmado == 'S': confirmado = True
    else: confirmado = False
    n_idcli = int(input('Insira o novo id do cli: '))
    n_idServ = int(input('Insira o novo id do serv: '))
    
    NHorario.atualizar(id_hor, n_data, confirmado, n_idcli, n_idServ)
    NHorario.salvar()

  @classmethod
  def HorarioExcluir(cls):
    cls.HorarioListar()
    id = int(input("Insira o id do obj horario: "))
    NHorario.excluir(id)
    NHorario.salvar()

  @classmethod
  def HorariosCriar(cls):
    data = datetime.datetime.strptime(input('Insira a data: '), '%d/%m/%Y')

    h_inicial, m_inicial = map(int, input('Insira a hora inicial xx:xx : ').split(':'))
    
    hm_inicial = datetime.timedelta(hours=h_inicial, minutes=m_inicial)
    data1 = data + hm_inicial
    
    h_final, m_final = map(int, input('Insira a hora final xx:xx :').split(':'))
    hm_final = datetime.timedelta(hours=h_final, minutes=m_final)
    data2 = data + hm_final
    
    duracao = int(input('Qual a duração dos horários: '))
    
    duracao = datetime.timedelta(minutes=duracao)
    
    var = data1

    while var < data2:
      horario = Horario(0, var, False, 0, 0)
      NHorario.inserir(horario)
      var += duracao
    NHorario.salvar()
   
UI.Main()