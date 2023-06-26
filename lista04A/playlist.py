import datetime

class Playlist:
  def __init__(self, nome, descricao):
    self.__nome, self.__descricao= '', ''
    self.__musicas = []

    self.set_nome(nome)
    self.set_descricao(descricao)

  def set_nome(self, nome):
    self.__nome = nome

  def get_nome(self):
    return self.__nome

  def set_descricao(self, descricao):
    self.__descricao = descricao
  
  def inserir(self, p_musica):
    self.__musicas.append(p_musica)

  def listar(self):
    return self.__musicas

  def tempo_total(self):
    soma = datetime.timedelta(minutes=0, seconds=0)
    
    for i in self.__musicas:
      soma += i.get_duracao()

    return soma

  def __str__(self):
    return f'\n  {self.__nome}\n  --Descrição: {self.__descricao}\n  --Tempo Total: {self.tempo_total()}'
    
class Musica:
  def __init__(self, titulo, artista, album, duracao):
    self.__titulo, self.__artista, self.__album, self.__duracao = '', '', '', ''
    self.__datainclusão = None

    self.set_datainclusao()
    self.set_titulo(titulo)
    self.set_artista(artista)
    self.set_album(album)
    self.set_duracao(duracao)

  def set_titulo(self, titulo):
    self.__titulo = titulo

  def set_artista(self, artista):
    self.__artista = artista

  def set_album(self, album):
    self.__album = album

  def set_datainclusao(self):
    self.__datainclusão = datetime.datetime.now()

  def set_duracao(self, duracao):
    self.__duracao = datetime.timedelta(minutes=int(duracao[:2]), seconds=int(duracao[3:]))

  def get_duracao(self):
    return self.__duracao

  def get_titulo(self):
    return self.__titulo

  def play(self):
    return f' Agora tocando:\n {self.__titulo}\n Artista: {self.__artista}\n Album: {self.__album}'

  def __str__(self):
    return f'\n  {self.__titulo}\n  {self.__duracao}\n  -Artista: {self.__artista}\n  -Album: {self.__album}\n  -Data de inclusão: {self.__datainclusão.strftime("%Y-%m-%d")}'


class UI:
  
  
  def main():
    playlists_database, musicas_database = [], []
    playlist_selecionada, musica_selecionada = None, None
    tracos = '-' * 30

    comandos = '''Comandos
-------------------------------------------------------------
--> add_musica - Adcionar uma nova música a database
--> add_playlist - Adcionar uma nova playlist a database
--> include_song - Adciona uma música a uma playlist
    
--> list_playlists - Lista todas playlists criadas
--> list_musicas -  Lista todas as músicas adcionadas
--> list_mus_playlist - Lista as músicas de uma playlist
     
--> del_playlist (nome_da_playlist) - Deleta uma playlist
--> rm_mus (playlist) (mus) - Rmov uma música de uma playlist
    
--> play (nome_da_musica) - Toca uma música 
--> playlist_info - Mostra as informações de uma playlist

--> help - Mostra essa lista de comandos
--> E - Encerra o programa
-------------------------------------------------------------'''
    
    print(comandos)
    while True:

      entrada = input(' --> ').lower()
    # add commands
      if entrada == 'add_playlist':
        nova_playlist = Playlist(input(' Nome da playlist: '), input(' Descrição: '))
        print()
        playlists_database.append(nova_playlist)
        print(' Playlist adcionada com sucesso!\n')
        
      elif entrada == 'add_musica':
        nova_musica = Musica(input(' Título da música: '), input(' Artista: '), input(' Album: '), input(' Duração no formato mm:ss : '))
        print()
        musicas_database.append(nova_musica)
        print(' Música adicionada com sucesso!\n')
        
      elif entrada == 'include_song':
        musica_encontrada, playlist_encontrada = None, None
        nome_da_playlist = input(' Insira o nome da playlist (case sensitive): ')
        playlist_presente = False  
      
        for playlist in playlists_database:
          if playlist.get_nome() == nome_da_playlist:
            playlist_encontrada = playlist
            playlist_presente = True  
            nome_da_musica = input(' Playlist encontrada! Informe o nome da música: ')
            break  # Encerra o loop assim que a playlist for encontrada
      
        if not playlist_presente:
            print(' Essa playlist não está presente em nossa database ainda')
      
        if playlist_presente:
          for musica in musicas_database:
            if musica.get_titulo() == nome_da_musica:
              musica_encontrada = musica
              playlist_encontrada.inserir(musica_encontrada)
              print('\n Música adicionada à playlist com sucesso!\n')
              break  # Encerra o loop assim que a música for adicionada à playlist
    
          if not musica_encontrada:
              print(' Não há uma música na database com esse nome')
    
      # list commands
      elif entrada == 'list_musicas':
        print(f'\n{tracos}')
        print('  Músicas adcionadas')
        print(tracos)
        for i in musicas_database:
          print(i)
        print(f'\n{tracos}\n')
          
      elif entrada == 'list_playlists':    
        print(f'\n{tracos}')
        print('  Playlists adicionadas')
        print(tracos) 
        for i in playlists_database:
          print(i)        
        print(f'\n{tracos}\n')
        
      elif entrada == 'list_mus_playlist':
        nome_playlist = input(' Insira o nome da playlist (case sensitive):\n --> ')
        for playlist in playlists_database:
          if playlist.get_nome() == nome_playlist:
            musicas = playlist.listar()
            if musicas:
              for musica in musicas:
                print(musica)
              print()
            else:
              print('\n Não há músicas nessa playlist!')
            break
          else:
            print('\n Não há uma playlist com esse nome')
            
      elif 'del_playlist ' in entrada:
        n_playlist = entrada[13:]
        for playlist in playlists_database:
          if playlist.get_nome() == n_playlist:
            playlists_database.remove(playlist)
            print(' Playlist removida\n')

      elif 'rm_mus ' in entrada:
        
        for playlist in playlists_database:
          if playlist.get_nome() in entrada:
            for musica in playlist.listar():
              if musica.get_titulo() in entrada:
                playlist.listar().remove(musica)
                print(f' Música removida\n')
              
  
      elif 'play ' in entrada:
        nome_mus = entrada[5:]        
        for mus in musicas_database:
          if mus.get_titulo() == nome_mus:
            print(mus.play())
          else: print(' Música não encontrada\n')
            
      elif entrada == 'playlist_info':
        teste = input(' Insira o nome da playlist (case sensitive):\n -->')
        for playlist in playlists_database:
          if playlist.get_nome() == teste:
            playlist_selecionada = playlist
        if playlist_selecionada: 
          print(f' Playlist selecionada: {playlist_selecionada}')
        else: print('\n Não há uma playlist com esse nome')

      elif entrada == 'help':
        print(f'\n{comandos}')
            
      elif entrada == 'e': break
      else:
        print(' Comando inválido\n')
    
      
UI.main()