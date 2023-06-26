import datetime, math

data_atual = datetime.datetime.now()

data_fornecida = datetime.datetime(2006, 10, 20)

idade = data_atual- data_fornecida

anos = idade.days/365

meses = math.floor((anos - math.floor(anos))*12)
print(f'Anos: {math.floor(anos)}\nmeses: {meses}')