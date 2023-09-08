import datetime, math

class Paciente:
  def __init__(self, nome, cpf, telefone, nascimento):
    self.__nome, self.__cpf, self.__telefone, self.__nascimento = '', '', '', datetime.datetime(2003, 3, 13)
    
    self.set_nome(nome)
    self.set_cpf(cpf)
    self.set_telefone(telefone)
    self.set_nascimento(nascimento)
    
  def set_nome(self, nome):
    try:
      if nome.strip() != '':
        self.__nome = nome

      else: raise ValueError('O nome não pode ser vazio')
        
    except ValueError:
      print(ValueError)

  def set_cpf(self, cpf):
    try:
      if cpf.strip() != '':
        self.__cpf = cpf

      else: raise ValueError('O cpf não pode ser vazio')
    except ValueError:
      print(ValueError)

  def set_telefone(self, telefone):
    try:
      if telefone.strip() != '':
        self.__telefone = telefone

      else: raise ValueError('O telefone não pode ser vazio')
    except ValueError:
      print(ValueError)

  def set_nascimento(self, nascimento): #20/10/2006
    try:
      if nascimento.strip() != '':
        dia, mes, ano = map(int, nascimento.split('/'))
        
        self.__nascimento = datetime.datetime(ano, mes, dia)
      else: raise ValueError('O nascimento não pode ser vazio')
    except ValueError:
      print(ValueError)

  def get_cpf(self):
    return self.__cpf

  def idade(self):
    data_atual = datetime.datetime.now()
    print(f'Data atual: {data_atual}')
    idade = data_atual - self.__nascimento
    print(f'{idade}')
    anos = idade.days/365
    print(f'Anos: {anos}')
    
    meses = math.floor((anos - math.floor(anos))*12)
    return f'Idade: {math.floor(anos)} anos e {meses} meses'

  def __str__(self):
    return f'\nFicha do paciente\nNome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\n Data de Nascimento: {self.__nascimento.strftime("%d/%m/%Y")}'

class UI:
  def main():
    lista_pacientes = []
    comandos = '''Comandos
--> add_p - adciona um paciente
--> idade (cpf_do_paciente) - mostra a idade de um paciente
--> info (cpf_do_paciente) - Mostra os dados de um paciente
--> e - encerra o programa
    '''
    print(comandos)
    
    while True:
      entrada = input('--> ').lower()
      if entrada == 'add_p':
        paciente = Paciente(input('Nome: '), input('CPF: '), input('Telefone: '), input('Data de nascimento xx/xx/xxxx: '))
        lista_pacientes.append(paciente)
      elif 'idade' in entrada:
        for paciente in lista_pacientes:
          if paciente.get_cpf() == entrada.split()[1]:
            print(paciente.idade())
          else: print('CPF não encontrado')

      elif 'info' in entrada:
        for paciente in lista_pacientes:
          if paciente.get_cpf() == entrada.split()[1]:
            print(paciente)
          else: print('CPF não encontrado')
            
      elif entrada == 'e':
        break

      else: print('Comando Inválido\n')
      
UI.main()