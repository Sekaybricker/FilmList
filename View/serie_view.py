class SerieView:

    def __init__(self, CtrlSeries):
        self.ctrlSerie = CtrlSeries
        self.enumGenero = EnumGenero


    def telaSerie(self):
        print('')
            print('--------Tela Series--------')
            print('|Digite a opcão desejada:')
            print('|[1] - Inserir series')
            print('|[2] - Excluir serie')
            print('|[3] - Ordenar series')
            print('|[4] - Listar  series')
            print('|[0] - Sair')
            opcao = input('|Opção:')
            print('|--------------------------|')
            print('')
            if opcao == '1':
                self.inserirSerie()
                break
            elif opcao == '2':
                self.excluirSerie()
                break
            elif opcao == '3':
                self.ctrlSeries.ordenarSerie()
                break
            elif opcao == '4':
                self.ctrlSeries.listarSerie()
                break
            elif opcao == '0':
                sys.exit()
            elif opcao != '1' and '2' and '0' and '3' and '4':
                print('digite uma opção valida')
                self.telaSerie()

    def inserirSerie(self):
        print('')
        print('--------Inserir Serie--------')
        nome = input('Digite o nome da serie: ')
        nota = input('Digite uma nota: ')
        episodio = input('Digite o episodio')
        critica = input('Escreva uma critica: ')
        enumList = list(map(str, EnumGenero))
        print(enumList)
        genero = input('selecione a opção do genero: ')
        self.ctrlSeries.inserirSerie(self, nome, nota, episodio,critica,genero)

    def excluirFilme(self):
        print('')
        print('--------Excluir Serie--------')
        nome = input('Digite o nome do serie: ')
        print('Serie Removida')
        self.ctrlSeries.excluirSerie(SerieNome)
