class Ingresso:
    def __init__(self, filme, dia, horario, tipo):
        self.__filme, self.__dia, self.__horario, self.__tipo = '', '', 0, ''
        self.set_filme(filme)
        self.set_dia(dia)
        self.set_horario(horario)
        self.set_tipo(tipo)

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
        horas = int(self.__horario)
        minutos = int((self.__horario - horas) * 60)
        return f'{horas:02d}:{minutos:02d}'

    def get_tipo(self):
        return self.__tipo

    def valor_ingresso(self):
        self.valor_base = 0
        
        if self.__dia == 'qua': self.valor_base = 8
          
        elif self.__dia == 'seg' or 'ter' or 'qui':
            self.valor_base = 16
        
        elif self.__dia == 'sex' or 'sab' or 'dom':
            self.valor_base = 20


        if self.__horario >= 17:
            self.valor_base += self.valor_base/2

        if self.__tipo == 'Meia':
            self.valor_base /= 2
          
        return int(self.valor_base)
        
    def __str__(self):
        return f'----------------------\nIngresso CineIf\n\nFilme: {self.get_filme()}\nData: {self.get_dia()} {self.get_horario()}\nTipo: {self.get_tipo()}\nValor: R$ {self.valor_ingresso()},00\n----------------------'


class UI:
    @staticmethod
    def main():
  
        print('Qual o nome do filme')
        filme = input()
        print('Dia da semana (ex: qua)')
        dia_da_semana = input()
        print('Qual o horário (ex: 16:00)')
        horario = input()
        horas, min = map(int, horario.split(':'))
        horario = horas + min/60
        print('Qual o tipo da entrada (ex: meia)')
        tipo = input()
        tipo = tipo.capitalize()
        x = Ingresso(filme, dia_da_semana, horario, tipo)

        print(x)
        
UI.main()



        
        