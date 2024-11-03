class TelaDesenvolvedor():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self):
        print()
        print("--- DESENVOLVEDOR ---")
        print("1 - Compartilhar jogo")
        print("2 - Lista de jogos desenvolvidos")
        print("3 - Editar Perfil")
        print("4 - Sair")

        #opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
        opcao = int(input())
        return opcao
    
    def mostrar_jogos(self, jogos):
        print()
        if len(jogos) > 0:
            print("Aqui está a lista de jogos que você criou")
            for jogo,c in jogos:
                print(f"{c - jogo}")
        else:
            print("Você ainda não criou nenhum jogo")