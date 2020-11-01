from Model.conteudo import Conteudo
from Model.enumGenero import EnumGenero


class Series(Conteudo):

    def __init__(self, nome: str, nota: int, critica: str, episodios: int, genero: EnumGenero, series: []):
        super().__init__(nome, nota, critica, genero)
        self.__episodios = episodios
        self.__series = series

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
    def episodios(self):
        return self.__episodios

    @episodios.setter
    def episodios(self, episodios):
        self.__episodios = episodios
        
    def insereSerie(self,nome,nota,episodios,critica,genero):
      series = Series(nome,nota,episodios,critica,genero)
      self.__series.append(series)     
