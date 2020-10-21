from Model.filmes import Filmes
from Model.series import Series
from View.viewPrincipal import ViewPrincipal
from Controller.ctrl_filmes import CtrlFilmes
from Controller.ctrl_series import CtrlSeries


class CtrlPrincipal:

    def __init__(self):
        self.Model = Filmes
        self.model = Series
        self.Controller = CtrlFilmes()
        self.Controller = CtrlSeries()
        self.view = ViewPrincipal()

    def telaPrincipal(self):
        ViewPrincipal.telaInicial(self)
