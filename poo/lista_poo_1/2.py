class Disciplina:
    def __init__(self, nome_da_disciplina, n1, n2, n3, n4, pfinal = 0):
        self.disciplina = nome_da_disciplina
        self.n1, self.n2, self.n3, self.n4, self.pfinal = n1, n2, n3, n4, pfinal

    def calc_media(self):
        self.media = (self.n1*2+self.n2*2+self.n3*3+self.n4*3)/10

        if self.pfinal != 0:
            self.media = (self.media + self.pfinal)/2
        
        return print(f'Disciplina: {self.disciplina}\nMédia: {self.media}')

sociologia = Disciplina('Sociologia', 100, 100, 90, 100)

sociologia.calc_media()