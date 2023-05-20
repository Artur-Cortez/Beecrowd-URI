class Ingresso:
    def __init__(self, filme, dia, horario, tipo):
        self.__filme, self.__dia, self.__horario, self.__tipo = filme, dia, horario, tipo

    def set_filme(self, filme):
        if filme != '': self.__filme = filme
        else: raise ValueError()        

    def set_dia(self, dia):
        dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
        if dia in dias: self.__dia = dia
        else: raise ValueError()
    
    def set_horario(self, horario):
        if horario != '': self.__horario = horario
        else: raise ValueError()

    def set_tipo(self, tipo):
        if tipo == 'Inteira' or 'Meia': self.__tipo = tipo
        else: raise ValueError()

    def get_filme(self):
        return self.__filme
    
    def get_dia(self):
        return self.__dia

    def get_horario(self):
        return self.__horario

    def get_tipo(self):
        return self.__tipo

    def valor_ingresso(self):
        self.valor_base = 0

        self.horar = self.__horario.split(':')
        self.horas = int(self.horar[0]) + int(self.horar[1])/60
        
        if self.__dia == 'seg' or 'ter' or 'qui':
            self.valor_base = 16
        
        elif self.__dia == 'sex' or 'sab' or 'dom':
            self.valor_base = 20

        else: self.valor_base = 8

        if self.horas >= 17:
            self.valor_base += self.valor_base/2

        if self.__tipo == 'Meia':
            self.valor_base /= 2

        

        return print(f'----------------------\nIngresso CineIf\n\nFilme: {self.__filme}\nData: {self.__dia} {self.__horario}\nTipo: {self.__tipo}\nValor: R$ {int(self.valor_base)},00\n----------------------')


class UI:
    @staticmethod
    def main():
        ingresso_barbie = Ingresso('Barbie o filme', 'seg', '16:00', 'Meia')
        ingresso_barbie.valor_ingresso()
        
UI.main()



        
        