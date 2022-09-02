import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar()#Método que realizar a conexão com o BD
        self.con = self.db_connection.cursor()#Navegação no banco de dados
    def inserir(self, musica, artista, album):
        try:
            sql = "insert into musicas(cod, musica, artista, album) values('','{}','{}','w{}')".format(musica, artista, album)
            self.con.execute(sql)
            self.db_connection.commit()#Insere o dado no banco de dados
            return "{} linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro