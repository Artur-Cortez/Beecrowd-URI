import datetime, json

# data_e_hora = input("Data e hora no formato dd/mm/yyyy hh/mm: ")
# data_formatada = datetime.datetime.strptime(data_e_hora, '%d/%m/%Y %H:%M')

# print(data_formatada)
# data_formatada += datetime.timedelta(hours=1)



# print(data_formatada)


# data = datetime.datetime.today() + datetime.timedelta(days=1)
# delta = datetime.timedelta(hours=15)

data_atual = datetime.datetime.today()

fuso = datetime.timedelta(hours=-3)
data_atual += fuso
hor= 8
if data_atual.hour > 18:
  delta = datetime.timedelta(days=1)
  data_atual += delta

nova_data = data_atual.replace(hour=hor, minute=0, second=0, microsecond=0)

print(nova_data)