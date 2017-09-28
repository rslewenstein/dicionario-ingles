
from condb import DBconecta

class Palavras(object):

    def __init__(self, idpalavra=0, palavra="", traducao="", exemplo=""):

        self.info = {}
        self.idpalavra = idpalavra
        self.palavra = palavra
        self.traducao = traducao
        self.exemplo = exemplo

    def inserirPalavra(self):

        db = DBconecta()
        try:

            p = db.conexao.cursor()
            p.execute("insert into palavras(palavra, traducao, exemplo) values('"+ self.palavra +"', '"+ self.traducao +"', '"+ self.exemplo +"')")
            db.conexao.commit()
            db.close()

            return "Palavra cadastrada com sucesso!"
        except:
            return "Ocorreu um erro ao cadastrar a palavra"


    def atualizarPalavra(self):
        db = DBconecta()
        try:
            p = db.conexao.cursor()
            p.execute("update palavras set palavra = '"+ self.palavra +"', traducao = '"+ self.traducao +"', exemplo = '"+ self.exemplo +"' where idpalavra = "+ self.idpalavra +" ")
            db.conexao.commit()
            p.close()
            return "Palavra atualizada com sucesso!"
        except:
            return "Ocorreu um erro ao alterar a palavra"


    def apagarPalavra(self):
        db = DBconecta()
        try:

            p = db.conexao.cursor()
            p.execute("delete from palavras where idpalavra = "+ self.idpalavra +"")
            db.conexao.commit()
            p.close()
            return "Palavra excluída com sucesso!"
        except:
            return "Ocorreu um erro na excluir"


    def buscarPalavra(self, idpalavra): # idpalavra
        db = DBconecta()
        try:

            p = db.conexao.cursor()
            p.execute("select * from palavras where idpalavra = "+ idpalavra +"") #idpalavra

            for linha in p:
                self.idpalavra = linha[0]
                self.palavra = linha[1]
                self.traducao = linha[2]
                self.exemplo = linha[3]

            p.close()

            return "Busca feita com sucesso!"
        except:
            return "Erro ao selecionar o usuário"