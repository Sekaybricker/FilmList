from abc import ABC
from Model.enumGenero import EnumGenero


class Conteudo(ABC):

    def __init__(self, nome: str, nota: int, critica: str, genero: EnumGenero):
        self.__nome = nome
        self.__nota = nota
        self.__critica = critica
        self.__genero = genero

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
