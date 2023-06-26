class Cliente:
  def __init__(self, nome, cpf, limite, socio="nenhum"):
    self.__nome, self.__cpf, self.__limite, self.__socio = '', '', 0.0, ''

    self.set_nome(nome)
    self.set_cpf(cpf)
    self.set_limite(limite)
    self.set_socio(socio)

  def set_nome(self, nome):
    try:
      if nome.strip() != '':
        self.__nome == nome
      else: raise ValueError('Nome não pode ser vazio')
    except ValueError: print(ValueError)

  def set_cpf(self, cpf):
    try:
      if cpf.strip() != '':
        self.__cpf = cpf
      else: raise ValueError('cpf não pode ser vazio')
    except ValueError: print(ValueError)

  def set_limite(self, limite):
    try:
      if limite > 0:
        self.__limite == limite
      else: raise ValueError('limite não pode ser vazio')
    except ValueError: print(ValueError)

  def set_socio(self, socio):
    try:
      if socio.strip() != '':
        self.__socio == socio
        if self._socio != 'nenhum':
          self.__limite += socio.get_limite()
      else: raise ValueError('Nome do sócio não pode ser vazio')
    except ValueError: print(ValueError)

  def get_limite(self):
    return self.__limite

  def __str__(self):
    return f'Nome: {self.__nome}\nCPF: {self.__cpf}\n Limite:{self.__limite}\nSócio: {self.__socio}'

class Empresa:
  def __init__(self, lista_clientes):
    self.__clientes = []

  def inserir(self, cliente):
    self.__clientes.append(cliente)

  def listar(self):
    return self.__clientes

class Empresa:
  def __init__(self, nome):
    self.__clientes = []
    self.__nome = nome

  def set_nome(self, nome):
    try:
      if nome.strip() != '':
        self.__nome = nome
      else: raise ValueError('O nome não pode ser vazio')
    except ValueError:
      print(ValueError)

  def get_nome(self):
    return self.__nome
  def inserir(self, cliente):
    self.__clientes.append(cliente)

  def listar(self):
    return self.__clientes


class UI:
  def main():
    lista_clientes, lista_empresas = [], []
    cmd = '''Comandos
    add_cliente - Adiciona cliente
    add_empresa - Adiciona empresa
    inserir (empresa) (cliente)
    '''
    entrada = input()

    if entrada == 'add_cliente':
     novo_cliente = Cliente(input('Nome: '), input('CPF: '), float(input('Limite: ')))
     lista_clientes.append(novo_cliente)
    elif entrada == 'add_empresa':
      nova_empresa = Empresa()
      lista_empresas.append(nova_empresa)
    elif 'inserir' in entrada:
      for empresa in lista_empresas:
        if empresa.get_nome() == entrada.split()[1]:
          for 


UI.main()