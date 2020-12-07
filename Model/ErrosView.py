class ErrosView(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Erro, {0} '.format(self.message)
        else:
            return 'Aconteceu um erro'

    def TypeError(self):
        return 'Insira um valor valido'


#raise ErrosView('Aconteceu um erro')
