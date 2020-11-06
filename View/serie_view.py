class SerieView:

    def __init__(self, CtrlSeries):
        self.ctrlSerie = CtrlSeries

    def telaSerie(self):
        print('')
        print('--------Excluir Serie--------')
        nome = input('Digite o nome da serie: ')
        print('Serie Removida')
        self.ctrlSeries.excluirSerie(nome)
