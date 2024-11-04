#Tela para criar o jogo, e nao para jogar
class TelaJogo():
    def __init__(self) -> None:
        pass

    def criar_jogo(self, dev):
        print()
        print(" --- Criando seu jogo --- ")
        titulo = input("Digite o titulo do jogo: ")
        genero = input("Digite o genero do jogo: ")
        descricao  = input("Qual a descricao do jogo?")
        idade = int(input("Digite a idade minima para jogar o jogo"))
        armazenamento = input("Espaço de armazenamento necessario: ")
        print()
        return {"titulo":titulo,
                "autor":dev.nome_de_usuario,
                "genero":genero,
                "descricao":descricao,
                "idade_minima":idade,
                "armazenamento":armazenamento
                }
    
    def listar_repositorio(self, repositorio):
        print()
        if len(repositorio) > 0:
            for jogo in repositorio:
                print(jogo.titulo)
                print(jogo.biografia_jogo)
                print(jogo.armazenamento)
                print(" ------------- ")
                print()
        else:
            print("Não há jogos disponiveis no momento. Tente mais tarde")