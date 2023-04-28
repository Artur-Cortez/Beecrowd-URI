import math
calendario = {
    '1':'Janeiro',
    '2':'Fevereiro',
    '3':'Março',
    '4':'Abril',
    '5':'Maio',
    '6':'Junho',
    '7':'Julho',
    '8':'Agosto',
    '9':'Setembro',
    '10':'Outubro',
    '11':'Novembro',
    '12':'Dezembro' }

print("Informe o número do mês")

entrada = input()

mes = calendario[entrada]

if math.ceil(int(entrada)/3) == 1:
    trimestre = 'primeiro'
elif math.ceil(int(entrada)/3) == 2:
    trimestre = 'segundo'
elif math.ceil(int(entrada)/3) == 3:
    trimestre = 'terceiro'
else: trimestre = 'quarto'

print(f'O mês de {mes} é do {trimestre} trimestre do ano')