from Model.filmes import Filmes
from Model.series import Series
from View.viewPrincipal import ViewPrincipal


class CtrlPrincipal:

    def __init__(self):
        self.Model = Filmes
        self.model = Series
        self.view = ViewPrincipal()

    def telaPrincipal(self):
        ViewPrincipal.telaInicial(self)
