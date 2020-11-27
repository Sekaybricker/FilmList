from Model.filmes import Filmes
from View.filme_View import FilmeView


class CtrlFilmes:

    def __init__(self, CtrlPrincipal):
        self.filmeView = FilmeView(self)
        self.ctrlPrincipal = CtrlPrincipal
        self.filmes = Filmes
        self.filmesList = []

    def __str__(self):
        return self.filmesList

    def telaFilme(self):
        self.filmeView.telaFilme()

    def inserirFilme(self, nome, nota, critica, genero, duracao):
        filme = Filmes(nome, nota, critica, genero, duracao)
        self.filmesList.append(filme)
        print((self.filmesList[0]))
        self.filmeView.telaFilme()

    def excluirFilme(self, filmeNome):
        self.filmesList.remove(filmeNome)
        self.filmeView.telaFilme()

    def ordenarfilme(self):
        self.filmeView.telaFilme()

    def editarFilme(self):
        self.filmeView.telaFilme()

    def listarFilme(self):
        print('[%s]' % ', '.join(map(str, self.filmesList)))
        self.filmeView.telaFilme()

    def telaInicial(self):
        self.ctrlPrincipal.telaPrincipal()
