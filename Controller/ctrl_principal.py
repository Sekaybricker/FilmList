from Model.filmes import Filmes
from Model.series import Series
from View.viewPrincipal import ViewPrincipal
from Controller.ctrl_filmes import CtrlFilmes
from Controller.ctrl_series import CtrlSeries


class CtrlPrincipal:

    def __init__(self):
        self.model = Filmes
        self.model = Series
        self.ctrlFilme = CtrlFilmes()
        self.ctrlSerie = CtrlSeries()
        self.view = ViewPrincipal(self)

    def telaPrincipal(self):
        self.view.telaInicial()
        print('inserido')

    def telaFilme(self):
        self.ctrlFilme.telaFilme()

    def telaSerie(self):
        self.ctrlSerie.telaSerie()
