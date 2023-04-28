def maior(x, y, z):
    maior = 0
    if x > y and x > z:
        maior = x
    if y > x and y > z:
        maior = y
    if z > x and z > y:
        maior = z
    return print(maior)

a, b, c = map(int, input('Insira três valores: ').split())
maior(a, b, c)
