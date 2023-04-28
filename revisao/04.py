print("Digite o primeiro horário no formato hh:mm")
h1, m1 = map(int, input().split(":"))

print("Digite o segundo horário no formato hh:mm")
h2, m2 = map(int, input().split(":"))


horas = h1 + h2

minutos = m1 + m2
if m1 + m2 >=60:
    minutos = max(m1,m2)%min(m1,m2)
    horas += 1

print(f'Total de horas: {horas}:{minutos}')