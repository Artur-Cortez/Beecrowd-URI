print('Digite o horario no formato hh:mm')
h, m = map(int, input().split(':'))

if h >= 0 and h <= 23 and m >= 0 and m <= 59:
    print('Hora válida')
    if h > 12:
        h -= 12
    print(h, m)
    ponteiro_horas = 30 * h + 0.5 * m #posicao do ponteiro das horas
    ponteiro_minutos = 6 * m #posicao do ponteiro dos minutos
    print(f'Ponteiro das horas: {ponteiro_horas}')
    print(f'Ponteiro dos minutos: {ponteiro_minutos}')
    print(f"Angulo entre ponteiros: {max(ponteiro_horas, ponteiro_minutos) - min(ponteiro_horas, ponteiro_minutos)}")

else: print('Hora inválida')
