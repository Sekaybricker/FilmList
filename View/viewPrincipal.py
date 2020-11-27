import PySimpleGUI as sg


class ViewPrincipal:

    def __init__(self, CtrlPrincipal):
        self.CtrlPrincipal = CtrlPrincipal

    def telaInicial(self):
        sg.theme('DarkTanBlue')
        layout = [
            [sg.Text('Selecione a tela que deseja acessar')],
            [sg.Button('Filmes'), sg.Button('Series')]
        ]
        tela1 = sg.Window('Tela inicial FilmList', layout, default_button_element_size=(15, 2),
                          auto_size_buttons=False, grab_anywhere=False, finalize=True)
        while True:
            window, event, value = sg.read_all_windows()
            if window == tela1 and event == sg.WIN_CLOSED:
                break
            if window == tela1 and event == 'Filmes':
                tela1.close()
                self.CtrlPrincipal.telaFilme()
            if window == tela1 and event == 'Series':
                tela1.close()
                self.CtrlPrincipal.telaSerie()
