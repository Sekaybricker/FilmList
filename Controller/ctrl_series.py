from View.serie_view import SerieView


class CtrlSeries:

    def __init__(self, CtrlPrincipal):
        self.ctrlPrincipal = CtrlPrincipal
        self.serieView = SerieView(self)

    def telaSerie(self):
        self.serieView.telaSerie()
