class TelaPerfil():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self):
        print()
        print(" ----- PERFIL ----- ")
        print("O que você deseja alterar no seu perfil ?")
        print("1 - Nome de usuario")
        print("2 - Senha")
        print("3 - Biografia")
        print("4 - Sair")
        opcao = int(input())
        return opcao

    def msg(self,msg):
        print(msg)

    def mudar_nome(self, usuario_atual):
        novo_nome = input()

    def mudar_senha(self):
        senha_atual = input("Digite sua senha atual: ")
        nova_senha = input("Digite sua nova senha")
        return {"nova_senha":nova_senha, "senha_atual":senha_atual}
