entrada = input('Insira seu nome completo: ').split()

def formatar_nome(nome):
    for i in nome:
        i[0].upper()
        print(i, end=' ')

formatar_nome(entrada)