senha = []

valores = input().split()

for i in range(10):
    digito = float(valores[i])
    senha.append({'digito': digito, 'posicao': i})


print(senha)