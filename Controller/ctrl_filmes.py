from Model.filmes import Filmes
from View.filme_View import FilmeView


class CtrlFilmes:

    def __init__(self):
        self.filmeView = FilmeView(self)
        self.filmes = Filmes()

    def telaFilme(self):
        self.filmeView.telaFilme()

    def inserirFilme(self, nome, nota, critica, genero, duracao):
        self.filmes.insereFilme(nome, nota, critica, genero, duracao)
        self.filmeView.telaFilme()

    def excluirFilme(self):
        print('excluir')
        self.filmeView.telaFilme()

    def ordenarfilme(self):
        print('ordena')
        self.filmeView.telaFilme()

    def listarFilme(self):
        print('lista')
        self.filmeView.telaFilme()
