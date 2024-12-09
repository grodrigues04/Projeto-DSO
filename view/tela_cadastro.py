from datetime import datetime
from .tela_abstrata import AbstractView
import PySimpleGUI as sg
class TelaCadastro(AbstractView):
    def __init__(self) -> None:
        super().__init__()
    
    def configurar_tela():
        layout = [
            [sg.Text("Digite seu nome de usuario"),sg.InputText("", key="nome_de_usuario")],
            [sg.Text("Digite sua senha"),sg.InputText("", key="senha_1", password_char="*")],
            [sg.Text("Confirme sua senha"),sg.InputText("", key="senha_2", password_char="*")],
            [sg.Text("Monte sua biografia"),sg.InputText("", key="biografia")],
            [sg.Text("", size=(40, 1), text_color="red", key="-MENSAGEM-")],
            [sg.Button("OK")] 
            ]

        return layout

    def configurar_tela_jogador(self, tipo_de_conta):
        self.__layout.append([sg.Text("Qual seu gênero"),sg.InputText("", key="senha_1", password_char="*")])
        self.__layout.append([sg.InputText("Qual seu ano de nascimento"),sg.InputText("", key="senha_1", password_char="*")])

    def configurar_tela_desenvolvedor(self, tipo_de_conta):
        self.__layout.append([sg.Text("Qual seu Email"),sg.InputText("", key="senha_1", password_char="*")])
        self.__layout.append([sg.InputText("Qual seu ano de nascimento"),sg.InputText("", key="senha_1", password_char="*")])
        self.__layout.append()

        window = sg.Window('Tela de Cadastro', layout, finalize=True)
        return window

    def rodar(self, tipo_de_conta, mensagem=None):
        window = self.configurar_tela(tipo_de_conta)
        event, values = self.abrir_tela(window, "password", mensagem)
        return (event, values)

