from model import model

class control:
    def __init__(self):
        self.musica = input('escreva uma musica')
        self.artista = input('escreva o nome do artista')
        self.album = input('album que esta musica pertence')
        print('{} de {} pertence ao album {}'.format(self.musica, self.artista,self.album))

