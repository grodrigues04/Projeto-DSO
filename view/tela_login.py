#Essa tela tem que ser chamada apos o cadastro, 
#E apos o login, chamar a tela que varia de acordo com a entidade(jogador,dev) com as opções de navegação
from .tela_abstrata import AbstractView
import PySimpleGUI as sg
class TelaLogin(AbstractView):

    def __init__(self) -> None:
        super().__init__()
    
    def mensagem(self,mensagem):
        print(mensagem)

    def configurar_tela(self, tipo_de_conta):

        layout = [
            [sg.Text(f"Tela de Login - {tipo_de_conta} ")],
            [sg.Text("Digite seu login")],
            [sg.InputText("")],
            [sg.Text("Digite sua Senha")],
            [sg.InputText("")],
            [sg.Button("ok")]
        ]
        window = sg.Window('Tela de Login', layout)
        return window
    
    def rodar(self, window, tipo_de_conta):
        window = self.configurar_tela(tipo_de_conta)
        event, values = self.abrir_tela(window)
        return {"event":event, "values":values}
