import sys
import PySimpleGUI as sg
from Model.ErrosView import ErrosView


class SerieView:

    def __init__(self, CtrlSeries):
        self.ctrlSeries = CtrlSeries
        self.ErrosView = ErrosView()
        self.lista: []

    def telaSerie(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Inserir Serie'), sg.Button('Remover Serie')],
            [sg.Button('listar Series'), sg.Button('Editar Serie')],
            [sg.Button('Ordenar Series'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Series', layout, default_button_element_size=(15, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Inserir Serie':
                tela1.hide()
                self.inserirSerie()
            if window == tela1 and event == 'Remover Serie':
                tela1.hide()
                self.excluirSerie()
            if window == tela1 and event == 'listar Series':
                tela1.hide()
                self.listarSerie()
            if window == tela1 and event == 'Editar Serie':
                tela1.hide()
                self.editarSerie()
            if window == tela1 and event == 'Ordenar Series':
                tela1.hide()
                self.ordenarSerie()
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.ctrlSeries.telaInicial()

    def inserirSerie(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Adicionar Serie')],
            [sg.Text('Nome:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Nota:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Critica:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Gênero:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('Duração:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Cadastrar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Series', layout, default_button_element_size=(10, 2),
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
                self.ctrlSeries.inserirSerie(nome, nota, critica, genero, duracao)

            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaSerie()

    def excluirSerie(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione o Serie a ser excluido')],
            [sg.Output(size=(40, 40))],
            [sg.Text('Nome:', size=(6, 1), key=('nome')), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Excluir'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Series', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        print(self.ctrlSeries.SeriesList)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Excluir':
                tela1.close()
                nome = value[0]
                self.ctrlSeries.excluirSerie(nome)
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaSerie()

    def listarSerie(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Todos os Series cadastrados')],
            [sg.Output(size=(40, 40))],
            [sg.Button('listar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Series', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'listar':
                print(str(self.ctrlSeries.SeriesList[it]))

            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaSerie()

    def editarSerie(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione o Serie a ser editado')],
            [sg.Output(size=(40, 40))],
            [sg.Text('Nome:', size=(6, 1)), sg.Input(size=(25, 1))],
            [sg.Text('    '), sg.Button('Atualizar'), sg.Button('Voltar')]
        ]
        tela1 = sg.Window('Gerenciamento De Series', layout, default_button_element_size=(10, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        print(self.ctrlSeries.SeriesList)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Atualizar':
                tela1.close()
                nome = value[0]
                self.ctrlSeries.excluirSerie(nome)
                self.inserirSerie()
            if window == tela1 and event == 'Voltar':
                tela1.close()
                self.telaSerie()
