def ordena(senha, tam):
    i = 1
    while i < tam:
        j = i - 1
        pivo = senha[i]
        while j >= 0 and senha[j]['digito'] < pivo['digito']:
            senha[j + 1] = senha[j]
            j -= 1
        senha[j + 1] = pivo
        i += 1

qtsCasos = 0
senha = []

while True:
    try:
        qtsDigitos = int(input())
        valores = input().split()

        for i in range(10):
            digito = float(valores[i])
            senha.append({'digito': digito, 'posicao': i})

        ordena(senha, 10)

        qtsCasos += 1
        print(f"Caso {qtsCasos}: ", end="")
        for i in range(qtsDigitos):
            print(senha[i]['posicao'], end="")

        print()
        senha = []

    except EOFError:
        break
