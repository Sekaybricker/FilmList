from Model.filmes import Filmes
from View.filme_View import FilmeView


class CtrlFilmes:

    def __init__(self):
        self.filmeView = FilmeView(self)
        self.filmes = Filmes
        self.filmesList = []

    def telaFilme(self):
        self.filmeView.telaFilme()

    def inserirFilme(self, nome, nota, critica, genero, duracao):
        filme = Filmes(nome, nota, critica, genero, duracao)
        self.filmesList.append(filme)
        self.filmeView.telaFilme()

    def excluirFilme(self, filmeNome):
        self.filmesList.remove(filmeNome)
        self.filmeView.telaFilme()

    def ordenarfilme(self):
        self.filmeView.telaFilme()

    def listarFilme(self):
        print('[%s]' % ', '.join(map(str, self.filmesList)))
        self.filmeView.telaFilme()
