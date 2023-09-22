import datetime

from primeiro import Horario

lista = []

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
  lista.append(horario)
  var += duracao

print(lista)
  
# duracao = input('Insira a duração: ') #timedelta