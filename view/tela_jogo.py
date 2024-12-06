#Tela para criar o jogo, e nao para jogar
from .tela_abstrata import AbstractView
class TelaJogo(AbstractView):
    def __init__(self) -> None:
        super().__init__()

    def criar_jogo(self):
        print()
        print(" --- Criando seu jogo --- ")
        titulo = input("Digite o titulo do jogo: ")
        genero = input("Digite o genero do jogo: ")
        descricao  = input("Qual a descricao do jogo?")
        idade = self.le_num_inteiro("Digite a idade minima para jogar o jogo")
        armazenamento = input("Espaço de armazenamento necessario: ")
        print()
        return {"titulo":titulo,
                "genero":genero,
                "descricao":descricao,
                "idade_minima":idade,
                "armazenamento":armazenamento
                }
    
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