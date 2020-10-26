from Model.conteudo import Conteudo
from Model.enumGenero import EnumGenero


class Filmes(Conteudo):

    def __init__(self, nome: str, nota: int, critica: str, duracao: int, genero: EnumGenero):
        super().__init__(nome, nota, critica, genero)
        self.__duracao = duracao
        self.__filmes = []

    def insereFilme(self, nome, nota, critica, genero, duracao):
        filme = Filmes(nome, nota, critica, genero, duracao)
        self.__filmes.append(filme)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def critica(self):
        return self.__critica

    @critica.setter
    def critica(self, critica):
        self.__critica = critica

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao
