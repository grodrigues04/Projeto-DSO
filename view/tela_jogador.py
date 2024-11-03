class TelaJogador():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self):
        print("--- JOGADOR ---")
        print("1 - Comprar jogo")
        print("2 - Ver sua lista de Jogos")
        print("3 - Editar Perfil")
        print("4 - Sair")
        #opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
        opcao = int(input())
        return opcao
    
    def mostrar_jogos(self, jogos):
        print()
        if len(jogos) > 0:
            print("Aqui está sua lista de jogos")
            for jogo,c in jogos:
                print(f"{c - jogo}")
        else:
            print("Você ainda não adquriu nenhum jogo")

    def adquirir_jogo(self):
        pass