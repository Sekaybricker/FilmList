from Model.conteudo import Conteudo


class Filmes(Conteudo):

    def __init__(self, nome: str, nota: int, critica: str, genero: str,duracao: int):
        super().__init__(nome, nota, critica, genero)
        self.__duracao = duracao

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
