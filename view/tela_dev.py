from .tela_abstrata import AbstractView
import PySimpleGUI as sg

class TelaDesenvolvedor(AbstractView):
    def __init__(self) -> None:
        super().__init__()

    def configurar_tela(self): #Arrumar dps
        layout = [
            [sg.Text("--- DESENVOLVEDOR ---", font=("Helvetica", 16), justification="center")],
            [sg.Button("Criar jogo", size=(25, 1))],
            [sg.Button("Lista de jogos desenvolvidos", size=(25, 1))],
            [sg.Button("Editar Perfil", size=(25, 1))],
            [sg.Button("Encerrar Sistema", size=(25, 1))],
            [sg.Button("voltar", size=(25, 1))],
        ]
        window = sg.Window('Tela dev', layout, finalize=True)
        return window
    
    def rodar(self, window):
        window = self.configurar_tela()
        #self.__ultima_tela = window
        event, values = self.abrir_tela(window)
        return {"event":event, "values":values}

