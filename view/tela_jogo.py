#Tela para criar o jogo, e nao para jogar
from .tela_abstrata import AbstractView
import PySimpleGUI as sg
class TelaJogo(AbstractView):
    def __init__(self) -> None:
        super().__init__()

    def configurar_tela(self, acao): #Arrumar dps
        if acao =="criar":
            window = self.criar_jogo()

        return window
    
    def criar_jogo(self):
        layout = [
            [sg.Text("Digite o título do jogo: "), sg.InputText(key="titulo")],
            [sg.Text("Digite o gênero do jogo: "), sg.InputText(key="genero")],
            [sg.Text("Qual a descrição do jogo?"), sg.InputText(key="descricao")],
            [sg.Text("Digite a idade mínima para jogar o jogo: "), sg.InputText(key="idade")],
            [sg.Text("Espaço de armazenamento necessário: "), sg.InputText(key="armazenamento")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Cadastro Jogo', layout, finalize=True)
        return window

    
    def listar_repositorio(self, repositorio):
        print()
        if len(repositorio) > 0:
            for jogo in repositorio:
                print()
                print(" ------------------------")
                print(f" - -- {jogo.titulo} -- - ")
                print(f"Autor: {jogo.autor}")
                print(f"Genero: {jogo.genero}")
                print(f"Descricao do jogo: {jogo.biografia_jogo}")
                print(f"Idade minima para jogar: {jogo.idade_minima}")
                print(f"Espaço de disco necessário: {jogo.armazenamento}")
                print(" ------------------------")
                print()
        else:
            print("Não há jogos disponiveis no momento. Tente mais tarde")


    def rodar(self, ação):
        window = self.configurar_tela(ação)
        #self.__ultima_tela = window
        event, values = self.abrir_tela(window)
        return {"event":event, "values":values}