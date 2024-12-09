from abc import ABC, abstractmethod
# import re
import PySimpleGUI as sg
# from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    def __init__(self):
        pass


    @abstractmethod
    def configurar_tela():
        pass

    #Fica responsavel por abrir as telas
    def abrir_tela(self, window, condicao_especial=None):
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'ok':
                break
            
            if condicao_especial!=None:

                if condicao_especial=="password":
                    senha = values["senha_1"]
                    confirma_senha = values["senha_2"]
                    if senha != confirma_senha:
                        sg.popup("A senhas não conferem")
                    else:
                        break

        window.close()
        print(event, values)
        return [event, values]

