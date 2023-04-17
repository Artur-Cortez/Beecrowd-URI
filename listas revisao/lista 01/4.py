print('Digite o primeiro horário no formato hh:mm')
hora1, minuto1 = map(int, input().split(':'))

print('Digite o segundo horário no formato hh:mm')
hora2, minuto2 = map(int, input().split(':'))

horas = 0
minutos = max(minuto1, minuto2) % min(minuto1, minuto2)
horas =  hora1 + hora2
if minuto1 + minuto2 >= 60:
    horas += 1
print(f'Total de horas = {horas}:{minutos}')