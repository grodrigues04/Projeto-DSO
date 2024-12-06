from .tela_abstrata import AbstractTela

class TelaJogador(AbstractTela):
    def __init__(self) -> None:
        super().__init__()


    def alterar_perfil(self):
        print()

    def msg(self,msg):
        print(msg)
        
    def tela_opcoes(self):
        print()
        print("--- JOGADOR ---")
        print("1 - Comprar jogo")
        print("2 - Ver sua lista de Jogos")
        print("3 - Editar Perfil")
        print("4 - Sair")
        print("5 - Tela inicial")
        print()
        #opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
        opcao = self.le_num_inteiro("Escolha uma opcao",[1,2,3,4,5])
        return opcao
    
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
            