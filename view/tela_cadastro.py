
from controller.cadastro_controller import Cadastro
class TelaCadastro:

    def confirma_senha(self):
        confirmaSenha = None
        print("Digite sua senha")
        senha = input()
        print("Confirme sua senha")
        while True:
            confirmaSenha = input()
            if senha!= confirmaSenha:
                print("A senhas não coincidem. Digite novamente")
            else:
                return senha
    
    def cadastrarDev(self):
        print("--- Criando sua conta de Desenvolvedor ---")
        print("Digite seu nome de usuário")
        login = input()
        senha = self.confirma_senha()
        print("Digite seu email")
        email = input()
        print("Você concorda com os termos [S/N] ?")
        termos = input()
        print("Deseja criar sua biografia agora [S/N]?")
        biografia = input()
        if biografia: #arrumar isso aqui para tratamento de excesspes
            print("Digite sua biografia")
            biografia = input()

        usuario_info = {"nome_de_usuario":login, "biografia":biografia, "email":email, "termos":termos, "senha":senha}
        Cadastro().cadastrar_usuario("desenvolvedor",usuario_info)

    def tipo_de_cadastro(self):
        usuario = {1:"jogador",2:self.cadastrarDev}
        print("Você quer criar uma conta de JOGADOR[1] ou DESENVOLVEDOR[2]")
        tipo_escolhido = usuario[int(input())]
        tipo_escolhido() # E se o usuario digitar uma letra?
    

TelaCadastro().tipo_de_cadastro()