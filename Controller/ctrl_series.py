from Model.series import Series
from View.serie_view import SerieView


class CtrlSeries:

    def __init__(self):
        self.serieView = SerieView(self)
        self.series = Series
        self.seriesList = []

    def telaSerie(self):
        self.serieView.telaSerie()

    def inserirSerie(self, nome, nota, episodios, critica, genero):
        series = Series(nome, nota, critica, episodios, genero)
        self.seriesList.append(series)
        self.serieView.telaSerie()

    def excluirSerie(self, serieNome):
        self.seriesList.remove(serieNome)
        self.serieView.telaSerie()

    def ordenaSerie(self):
        self.serieView.telaSerie()

    def listarSerie(self):
        print('[%s]' % ', '.join(map(str, self.seriesList)))
        self.serieView.telaSerie()
