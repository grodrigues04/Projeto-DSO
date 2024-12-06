from abc import ABC, abstractmethod
# import re
import PySimpleGUI as sg
# from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    def __init__(self):
        pass

    #Fica responsavel por abrir as telas
    def abrir_tela(self, window):
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'ok':
                break
        window.close()
        print(event, values)
        return [event, values]

    def iniciar_componentes(self, titulo, opções):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey15')
        layout = [
            [sg.Text(titulo, font=("Helvetica", 18))],
            [sg.Text('Escolha sua opção', font=("Arial", 14))]
        ]

        for k, value in sorted(opções.items()):
            if k != 0:
                layout.append([sg.Radio(value, "RD1", key=str(k))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Voltar')])
        return sg.Window('Sistema de cursos', layout)

    def open(self, window):
        button, values = window.Read()
        return button, values