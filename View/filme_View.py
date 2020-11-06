import sys
from Model.enumGenero import EnumGenero


class FilmeView:

    def __init__(self, CtrlFilmes):
        self.ctrlFilmes = CtrlFilmes
        self.enumGenero = EnumGenero

    def telaFilme(self):

        opcao = ''
        while opcao != '0':
            print('')
            print('--------Tela Filmes--------')
            print('|Digite a opcão desejada:')
            print('|[1] - Inserir filmes')
            print('|[2] - Excluir filme')
            print('|[3] - Ordenar filmes')
            print('|[4] - Listar  filmes')
            print('|[0] - Sair')
            opcao = input('|Opção:')
            print('|--------------------------|')
            print('')
            if opcao == '1':
                self.inserirFilme()
                break
            elif opcao == '2':
                self.excluirFilme()
                break
            elif opcao == '3':
                self.ctrlFilmes.ordenarfilme()
                break
            elif opcao == '4':
                self.ctrlFilmes.listarFilme()
                break
            elif opcao == '0':
                sys.exit()
            elif opcao != '1' and '2' and '0' and '3' and '4':
                print('digite uma opção valida')
                self.telaFilme()

    def inserirFilme(self):
        print('')
        print('--------Inserir Filme--------')
        nome = input('Digite o nome do filme: ')
        nota = input('Digite uma nota: ')
        critica = input('Escreva uma critica: ')
        enumList = list(map(str, EnumGenero))
        print(enumList)
        genero = input('selecione a opção do genero: ')
        duracao = input('Digite a duração em segundos: ')
        self.ctrlFilmes.inserirFilme(nome, nota, critica, genero, duracao)

    def excluirFilme(self):
        print('')
        print('--------Excluir Filme--------')
        nome = input('Digite o nome do filme: ')
        print('Filme Removido')
        self.ctrlFilmes.excluirFilme(nome)

