class Ingresso:
    def __init__(self, filme, dia, horario, tipo):
        self.filme, self.dia, self.horario, self.tipo = filme, dia, horario, tipo

    def valor_ingresso(self):
        self.valor_base = 0

        self.horar = self.horario.split(':')
        self.horas = int(self.horar[0]) + int(self.horar[1])/60
        
        if self.dia == 'Segunda' or 'Terça' or 'Quinta':
            self.valor_base = 16
        
        elif self.dia == 'Sexta' or 'Sábado' or 'Domiingo':
            self.valor_base = 20

        else: self.valor_base = 8

        if self.horas >= 17:
            self.valor_base += self.valor_base/2

        if self.tipo == 'Meia':
            self.valor_base /= 2

        

        return print(f'----------------------\nIngresso CineIf\n\nFilme: {self.filme}\nData: {self.dia} {self.horario}\nTipo: {self.tipo}\nValor: R$ {int(self.valor_base)},00\n----------------------')

ingresso_barbie = Ingresso('Barbie o filme', 'Segunda', '16:00', 'Meia')

ingresso_barbie.valor_ingresso()
        
        
