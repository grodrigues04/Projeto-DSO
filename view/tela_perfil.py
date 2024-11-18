from .tela_abstrata import AbstractTela
class TelaPerfil(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes(self):
        print()
        print(" ----- PERFIL ----- ")
        print("O que você deseja alterar no seu perfil ?")
        print("1 - Nome de usuario")
        print("2 - Senha")
        print("3 - Biografia")
        print("4 - Sair")
        opcao = self.le_num_inteiro("Escolha uma opcao", [0,1,2,3,4])
        return opcao

    def msg(self,msg):
        print(msg)

    def mudar_nome(self):
        print("Digite seu novo nome de usuario")
        novo_nome = input()
        return novo_nome

    def mudar_senha(self):
        senha_atual = input("Digite sua senha atual: ")
        nova_senha = input("Digite sua nova senha")
        return {"nova_senha":nova_senha, "senha_atual":senha_atual}
