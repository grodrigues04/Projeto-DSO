from abc import ABC, abstractmethod
# import re
import PySimpleGUI as sg
# from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    def __init__(self):
        self.__ultima_tela = None

    @property
    def ultima_tela(self):
        return self.__ultima_tela
    
    def exibir_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    @abstractmethod
    def configurar_tela():
        pass

    #Fica responsavel por abrir as telas
    def abrir_tela(self, window=None, condicao_especial=None, mensagem=None):
        self.__ultima_tela = window
        
        while True:
            if mensagem:
                window["-MENSAGEM-"].update(mensagem)

            event, values = window.read()
            print("EVENTO:", event)
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

