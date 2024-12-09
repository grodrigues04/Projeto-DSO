from datetime import datetime
from .tela_abstrata import AbstractView
import PySimpleGUI as sg
class TelaCadastro(AbstractView):

    def __init__(self) -> None:
        super().__init__()
    
    def configurar_tela(self):
        layout = [
            [sg.Text("Digite seu nome de usuario"),sg.InputText("", key="nome_de_usuario")],
            [sg.Text("Digite sua senha"),sg.InputText("", key="senha_1", password_char="*")],
            [sg.Text("Confirme sua senha"),sg.InputText("", key="senha_2", password_char="*")],
            [sg.Text("Monte sua biografia"),sg.InputText("", key="biografia")],
            [sg.Text("", size=(40, 1), text_color="red", key="-MENSAGEM-")],
        ]

        return layout

    def configurar_tela_jogador(self, layout):
        layout.append([sg.Text("Qual seu gênero"),sg.InputText("", key="genero")])
        layout.append([sg.Text("Qual seu ano de nascimento"),sg.InputText("", key="idade")])
        layout.append([sg.Button("OK")])

        window = sg.Window('Cadastro de jogador', layout, finalize=True)
        return window

    def configurar_tela_desenvolvedor(self, layout):
        layout.append([sg.Text("Qual seu Email"),sg.InputText("", key="email")])
        layout.append([sg.Text("Qual seu ano de nascimento"),sg.InputText("", key="senha_1", password_char="*")])
        layout.append([sg.Radio("Li e concordo com os termos","termos", key="concorda"), sg.Radio("Não li os termos","termos", key="concorda")])
        layout.append([sg.Button("OK")])

        window = sg.Window('Cadastro Desenvolvedor', layout, finalize=True)
        return window

    def rodar(self, tipo_de_conta, mensagem=None):
        opcoes_de_tela = {
            "desenvolvedor":self.configurar_tela_desenvolvedor,
            "jogador":self.configurar_tela_jogador
        }
        layout = self.configurar_tela()
        tela_que_vai_abrir = opcoes_de_tela[tipo_de_conta]
        window = tela_que_vai_abrir(layout)
        event, values = self.abrir_tela(window, "password", mensagem)
        return (event, values)

