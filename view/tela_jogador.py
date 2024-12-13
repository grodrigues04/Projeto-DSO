from .tela_abstrata import AbstractView
import PySimpleGUI as sg
class TelaJogador(AbstractView):
    def __init__(self) -> None:
        super().__init__()


    
    def alterar_perfil(self):
        print()

    def msg(self,msg):
        print(msg)
        
    def configurar_tela(self):
        layout = [
            [sg.Text('--- JOGADOR ---', font=("Helvetica", 16), justification='center')],
            [sg.Button('Comprar Jogo', size=(25, 1))],
            [sg.Button('Ver minha lista de Jogos', size=(25, 1))],
            [sg.Button('Editar Perfil', size=(25, 1))],
            [sg.Button('Sair', size=(25, 1))],
            [sg.Button('Tela Inicial', size=(25, 1))]
        ]

        window = sg.Window('Tela jogador', layout, finalize=True)
        return window
    
    def rodar(self, window):
        window = self.configurar_tela()
        event, values = self.abrir_tela(window)
        return {"event":event, "values":values}



    def mostrar_jogos(self, jogos):
        print()
        if len(jogos) > 0:
            print("Aqui está sua lista de jogos: ")
            for jogo in jogos: #arrumar essa merda
                print(f"titulo: {jogo.titulo}")
                print(f"autor:{jogo.autor}")
                print()
        else:
            print("Você ainda não adquriu nenhum jogo")

    def adquirir_jogo(self, repositorio_de_jogos):
        while True:
            print("Jogos disponiveis para a compra")
            c = 1
            for jogo in repositorio_de_jogos:
                print(f"Nome:- {jogo.titulo}")
                print(f"Autor:- {jogo.autor}")
                print(f"Gênero: {jogo.genero}")
                print(f"Descricão: {jogo.biografia_jogo}")
                print(f"Idade mínima: {jogo.idade_minima}")
                print()
                c+=1
            jogo_desejado = input("Digite o nome do jogo que voce quer comprar: ")
        
            for jogo in repositorio_de_jogos:
                if jogo.titulo.lower() == jogo_desejado.lower(): 
                    return jogo  # Retorna o objeto Jogo correspondente
                else:
                    print("Jogo não encontrado. Tente novamente.\n")
            