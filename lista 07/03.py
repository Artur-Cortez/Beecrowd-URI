def aprovado(nota1, nota2):
    media = (nota1+nota2)/2
    if media >= 60:
        return print('Aprovado')
    else: return print('Reprovado')