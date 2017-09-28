#coding: utf-8

# importando o módulo do SQLite
import sqlite3

class DBconecta():

    def __init__(self):
        self.conexao = sqlite3.connect('date.db')
        self.criaTabela()

    def criaTabela(self):

        t = self.conexao.cursor()

        t.execute("""create table if not exists palavras(
                    idpalavra integer primary key autoincrement, 
                    palavra text, 
                    traducao text, 
                    exemplo text)""")

        self.conexao.commit()
        t.close()