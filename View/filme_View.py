import sys
import PySimpleGUI as sg
from Model.ErrosView import ErrosView


class FilmeView:

    def __init__(self, CtrlFilmes):
        self.ctrlFilmes = CtrlFilmes
        self.ErrosView = ErrosView()
        self.lista: []

    def telaFilme(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Inserir Filme'), sg.Button('Remover Filme')],
            [sg.Button('listar Filmes'), sg.Button('Editar Filme')],
            [sg.Button('Ordenar Filmes'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Filmes', layout, default_button_element_size=(15, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Inserir Filme':
                tela1.hide()
                self.inserirFilme()
            if window == tela1 and event == 'Remover Filme':
                tela1.hide()
                self.excluirFilme()
            if window == tela1 and event == 'listar Filmes':
                tela1.hide()
                self.listarFilme()
            if window == tela1 and event == 'Editar Filme':
                tela1.hide()
                self.editarFilme()
            if window == tela1 and event == 'Ordenar Filmes':
                tela1.hide()
                self.ordenarfilme()
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.ctrlFilmes.telaInicial()

    def inserirFilme(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Adicionar Filme')],
            [sg.Text('Nome:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Nota:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Critica:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Gênero:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Duração:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Cadastrar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Filmes', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Cadastrar':
                nome = value[0]
                nota = value[1]
                critica = value[2]
                genero = value[3]
                duracao = value[4]
                try:
                    int(nota, duracao)
                except:
                    self.ErrosView.TypeError()
                tela1.close()
                self.lista = nome, nota, critica, genero, duracao
                self.ctrlFilmes.inserirFilme(nome, nota, critica, genero, duracao)

            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaFilme()

    def excluirFilme(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione o filme a ser excluido')],
            [sg.Output(size=(40, 40))],
            [sg.Text('Nome:', size=(6, 1), key=('nome')), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Excluir'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Filmes', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        print(self.ctrlFilmes.filmesList)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Excluir':
                tela1.close()
                nome = value[0]
                self.ctrlFilmes.excluirFilme(nome)
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaFilme()

    def listarFilme(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Todos os filmes cadastrados')],
            [sg.Output(size=(40, 40))],
            [sg.Button('listar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Filmes', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'listar':
                print(str(self.ctrlFilmes.filmesList[it]))

            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaFilme()

    def editarFilme(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione o filme a ser editado')],
            [sg.Output(size=(40, 40))],
            [sg.Text('Nome:', size=(6, 1), key=('nome')), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Atualizar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Filmes', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        print(self.ctrlFilmes.filmesList)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Atualizar':
                tela1.close()
                nome = value[0]
                self.ctrlFilmes.excluirFilme(nome)
                self.inserirFilme()
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaFilme()
