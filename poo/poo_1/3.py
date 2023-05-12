class Viagem:
    def __init__(self, distancia, tempo_gasto):
        self.distancia = distancia
        self.tempo_gasto = tempo_gasto

    def calc_velocidade_media(self):
        self.tempo_gasto = self.tempo_gasto.split(':')
        self.tempo = int(self.tempo_gasto[0]) + (int(self.tempo_gasto[1])/60)

        return print(f'Velocidade média: {self.distancia/self.tempo} Km/h')


natal_recife = Viagem(300, '03:00')

natal_recife.calc_velocidade_media()