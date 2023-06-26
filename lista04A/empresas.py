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

class UI:
  def main():
    cmd = '''Comandos
    add_cliente - Adciona
    add_empresa
    '''
    entrada = input().lower()

    if entrada == 'add'


UI.main()