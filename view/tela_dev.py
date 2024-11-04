class TelaDesenvolvedor():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self):
        print()
        print("--- DESENVOLVEDOR ---")
        print("1 - Criar jogo")
        print("2 - Lista de jogos desenvolvidos")
        print("3 - Editar Perfil")
        print("4 - Sair")
        print()
        #opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
        opcao = int(input())
        return opcao
    
    def mostrar_jogos(self, jogos):
        print()
        if len(jogos) > 0:
            print("Aqui está a lista de jogos que você criou")
            c = 1
            for jogo in jogos:
                print()
                print(" ------------------------")
                print(f"{c} - -- {jogo.titulo}  --")
                print(f"Autor: {jogo.autor}")
                print(f"Genero: {jogo.genero}")
                print(" ------------------------")
                print()
                c+=1
        else:
            print("Você ainda não criou nenhum jogo")