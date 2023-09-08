class Cliente:
  def __init__(self, nome, cpf, limite):
    self.__nome, self.__cpf, self.__limite, self.__socio = '', '', -1.0, 'nenhum'
    self.set_nome(nome)
    self.set_cpf(cpf)
    self.set_limite(limite)

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
   pass
    
  def get_limite(self):
    return self.__limite

  def get_cpf(self):
    return self.__cpf

  def __str__(self):
    return f'\n Nome: {self.__nome}\n CPF: {self.__cpf}\n Limite:{self.__limite}\n Sócio: {self.__socio}'

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
    lista_empresas = []
    cmd = '''Comandos
-------------------------------------------------------------------
--> add_empresa - Adiciona uma empresa a database
--> add_cliente (empresa) - Insere um cliente a uma empresa
--> listar_clientes (empresa) - Lista os clientes de uma empresa
--> set_sociedade (empresa) (cpf1) (cpf2) - Torna A e B sócios
--> help - mostra esses comandos
--> E - encerra o programa
-------------------------------------------------------------------'''
    print(cmd)
    while True:
      entrada = input(' --> ')
  
      if entrada == 'add_empresa':
        nova_empresa = Empresa(input(' Nome da empresa: '))
        lista_empresas.append(nova_empresa)
        print('\nEmpresa adicionada com sucesso!\n')
      
      elif 'add_cliente' in entrada:       
       for empresa in lista_empresas:
         if empresa.get_nome() == entrada.split()[1]:
          novo_cliente = Cliente(input(' Nome: '), input(' CPF: '), float(input(' Limite: ')))
          empresa.inserir(novo_cliente)
          print(' Cliente inserido com sucesso!\n')
         else: print(' Empresa não encontrada\n')
  
      elif 'listar_clientes' in entrada:
        for empresa in lista_empresas:
          if empresa.get_nome() == entrada.split()[1]:
            for i in empresa.listar(): print(i)
  

      elif 'set_sociedade' in entrada:
        for empresa in lista_empresas:
          if empresa.get_nome() == entrada.split()[0]:
            selecionada = empresa
            for j in selecionada.listar():
              if j.get_cpf() == entrada.split()[1]:
                cliente_a = j # primeiro cliente
            
            
            
            
  
      elif entrada == 'help': print(cmd)
      elif entrada == 'E' or entrada == 'e': break
      else: print(' Comando inválido\n')
  
    
UI.main()