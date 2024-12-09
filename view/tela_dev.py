from .tela_abstrata import AbstractView
class TelaDesenvolvedor(AbstractView):
    def __init__(self) -> None:
        pass

    def configurar_tela(): #Arrumar dps
        pass
    
    def tela_opcoes(self):
        print()
        print("--- DESENVOLVEDOR ---")
        print("1 - Criar jogo")
        print("2 - Lista de jogos desenvolvidos")
        print("3 - Editar Perfil")
        print("4 - Encerrar Sistema")
        print("5 - Tela inicial")
        print()
        #opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
        opcao = self.le_num_inteiro("Escolha uma opção",[1,2,3,4,5])
        return opcao
    
    def mostrar_jogos(self, jogos):
        print()
        if len(jogos) > 0:
            print("Aqui está a lista de jogos que você criou")
            c = 1
            for jogo in jogos:
                print()
                print(" ------------------------")
                print(f" - -- {jogo.titulo} -- - ")
                print(f"Genero: {jogo.genero}")
                print(f"Descricao do jogo: {jogo.biografia_jogo}")
                print(f"Idade minima para jogar: {jogo.idade_minima}")
                print(f"Espaço de disco necessário: {jogo.armazenamento}")
                print(" ------------------------")
                print()
                c+=1
        else:
            print("Você ainda não criou nenhum jogo")