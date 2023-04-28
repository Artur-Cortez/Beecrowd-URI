def maior(x, y):
    maior = 0
    if x > y:
        maior = x
    else: maior = y
    return print(maior)


a, b = map(int, input('Insira dois valores: ').split())
maior(a, b)