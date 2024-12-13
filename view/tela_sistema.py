import PySimpleGUI as sg
from .tela_abstrata import AbstractView

class TelaSistemaInicial(AbstractView):
    def __init__(self):
        super().__init__()

    def configurar_tela(self):
        layout = [  
            [sg.Text("Tela inicial")], 
            [sg.Radio("Realizar login", "entrar", key=1), sg.Radio("Realizar Cadastro", "entrar", key=2)],
            [sg.Text("Qual o tipo da conta?")], 
            [sg.Radio('Desenvolvedor',"conta", key="desenvolvedor"), sg.Radio('Jogador', "conta", key="jogador")],
            [sg.Button("ok")]
        ]
        window = sg.Window('Tela do Sistema', layout)
        return window
    
    def rodar(self):
        window = self.configurar_tela()
        # self.__ultima_tela = window
        event, values = self.abrir_tela(window)
        return (event, values)
        