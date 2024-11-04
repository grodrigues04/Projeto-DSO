class TelaJogador():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self):
        print()
        print("--- JOGADOR ---")
        print("1 - Comprar jogo")
        print("2 - Ver sua lista de Jogos")
        print("3 - Editar Perfil")
        print("4 - Sair")
        print()
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

    def adquirir_jogo(self, repositorio_de_jogos):
        while True:
            print("Jogos disponiveis para a compra")
            c = 1
            for jogo in repositorio_de_jogos:
                print(f"{c} - {jogo.titulo}")
                print(jogo.genero)
                print(jogo.biografia_jogo)
                print(jogo.idade_minima)
                print()
                c+=1
            jogo_desejado = input("Digite o nome do jogo que voce quer comprar")
        
            for jogo in repositorio_de_jogos:
                if jogo.titulo.lower() == jogo_desejado.lower():  # Compara títulos ignorando case
                    return jogo  # Retorna o objeto Jogo correspondente
                print("Jogo não encontrado. Tente novamente.\n")
            