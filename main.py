#coding: utf-8

from palavras import Palavras
from tkinter import *

class Application():

    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 30
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 30
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 40
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 15
        self.container7.pack()

        self.titulo = Label(self.container1, text="Cadastro de Palavras: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidpalavra = Label(self.container2, text="id Palavra:", font=self.fonte, width=10)
        self.lblidpalavra.pack(side=LEFT)

        self.txtidpalavra = Entry(self.container2)
        self.txtidpalavra["width"] = 5
        self.txtidpalavra["font"] = self.fonte
        self.txtidpalavra.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscar
        self.btnBuscar.pack(side=RIGHT)

        self.lblpalavra = Label(self.container3, text="Palavra:", font=self.fonte, width=10)
        self.lblpalavra.pack(side=LEFT)

        self.txtpalavra = Entry(self.container3)
        self.txtpalavra["width"] = 30
        self.txtpalavra["font"] = self.fonte
        self.txtpalavra.pack(side=LEFT)

        self.lbltraducao = Label(self.container4, text="Tradução:", font=self.fonte, width=10)
        self.lbltraducao.pack(side=LEFT)

        self.txttraducao = Entry(self.container4)
        self.txttraducao["width"] = 30
        self.txttraducao["font"] = self.fonte
        self.txttraducao.pack(side=LEFT)

        self.lblexemplo = Label(self.container5, text="Exemplo:", font=self.fonte, width=10)
        self.lblexemplo.pack(side=LEFT)

        self.txtexemplo = Entry(self.container5)
        self.txtexemplo["width"] = 30
        self.txtexemplo["font"] = self.fonte
        self.txtexemplo.pack(side=LEFT)

        self.btnInserir = Button(self.container6, text="Inserir", font=self.fonte, width=12)
        self.btnInserir["command"] = self.inserir
        self.btnInserir.pack(side=LEFT)

        self.btnAlterar = Button(self.container6, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterar
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container6, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluir
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserir(self):
        pal = Palavras()

        pal.palavra = self.txtpalavra.get()
        pal.traducao = self.txttraducao.get()
        pal.exemplo = self.txtexemplo.get()

        self.lblmsg["text"] = pal.inserirPalavra()

        self.txtidpalavra.delete(0, END)
        self.txtpalavra.delete(0, END)
        self.txttraducao.delete(0, END)
        self.txtexemplo.delete(0, END)


    def alterar(self):
        pal = Palavras()

        pal.idpalavra = self.txtidpalavra.get()
        pal.palavra = self.txtpalavra.get()
        pal.traducao = self.txttraducao.get()
        pal.exemplo = self.txtexemplo.get()


        self.lblmsg["text"] = pal.atualizarPalavra()

        self.txtidpalavra.delete(0, END)
        self.txtpalavra.delete(0, END)
        self.txttraducao.delete(0, END)
        self.txtexemplo.delete(0, END)

    def excluir(self):
        pal = Palavras()

        pal.idpalavra = self.txtidpalavra.get()

        self.lblmsg["text"] = pal.apagarPalavra()

        self.txtidpalavra.delete(0, END)
        self.txtpalavra.delete(0, END)
        self.txttraducao.delete(0, END)
        self.txtexemplo.delete(0, END)


    def buscar(self):
        pal = Palavras()

        idpalavra = self.txtidpalavra.get()

        self.lblmsg["text"] = pal.buscarPalavra(idpalavra)

        self.txtidpalavra.delete(0, END)
        self.txtidpalavra.insert(INSERT, pal.idpalavra)

        self.txtpalavra.delete(0, END)
        self.txtpalavra.insert(INSERT, pal.palavra)

        self.txttraducao.delete(0, END)
        self.txttraducao.insert(INSERT, pal.traducao)

        self.txtexemplo.delete(0, END)
        self.txtexemplo.insert(INSERT, pal.exemplo)

root = Tk()
Application(root)
root.mainloop()