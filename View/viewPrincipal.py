import sys


class ViewPrincipal:

    def __init__(self, CtrlPrincipal):
        self.CtrlPrincipal = CtrlPrincipal

    def telaInicial(self):
        opcao = ''
        while opcao != '0':
            print('')
            print('|-------Tela inicial-------|')
            print('|Digite a opcão desejada:')
            print('|[1] - Tela de filmes')
            print('|[2] - Tela de series')
            print('|[0] - Sair')
            opcao = input('|Opção:')
            print('|--------------------------|')
            print('')
            if opcao == '1':
                self.CtrlPrincipal.telaFilme()
                break
            elif opcao == '2':
                self.CtrlPrincipal.telaSerie()
                break
            elif opcao == '0':
                sys.exit()
            elif opcao != '1' and '2' and '0':
                print('digite uma opção valida')
                self.telaInicial()

