from controller.cadastro_controller import Cadastro
from datetime import datetime
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
    

    def cadastroGeral(self, tipo_de_conta, saudaçao):
        print(f"--- Criando sua conta de {saudaçao} ---")
        print("Digite seu nome de usuário")
        login = input()
        senha = self.confirma_senha()
        print("Digite seu email")
        email = input()
        print("Deseja criar sua biografia agora [S/N]?")
        biografia = input()
        if biografia=="S": #arrumar isso aqui para tratamento de exceções
            print("Digite sua biografia")
            biografia = input()

        tipo_de_conta(login, senha, biografia, email)


    def cadastrarDev(self, login, senha, biografia, email):
        print("Você concorda com os termos [S/N] ?")
        termos = input()
        print("Deseja criar sua biografia agora [S/N]?")
        usuario_info = {"nome_de_usuario":login, "biografia":biografia, "email":email, "termos":termos, "senha":senha}
        Cadastro().cadastrar_usuario("desenvolvedor",usuario_info)


    def cadastrarJogador(self, login, senha, biografia, email):
        ano_atual = datetime.now().year
        print("Qual seu Gênero? [M/F/OUTRO]")
        genero = input()
        print("Em que ano você nasceu ?")
        ano_nascido = int(input())
        idade = ano_atual - ano_nascido
        usuario_info = {"nome_de_usuario":login, "senha":senha,"genero":genero,"idade":idade, "biografia":biografia}
        Cadastro().cadastrar_usuario("jogador", usuario_info)

    def tipo_de_cadastro(self):
        tipos_de_usuario = {1:self.cadastrarJogador, 2:self.cadastrarDev}
        saudacao_usuario = {1:"Jogador", 2:"Desenvolvedor"}
        print("Você quer criar uma conta de JOGADOR[1] ou DESENVOLVEDOR[2]")
        tipo_escolhido = int(input())
        self.cadastroGeral(tipos_de_usuario[tipo_escolhido], saudacao_usuario[tipo_escolhido]) # E se o usuario digitar uma letra?
    

TelaCadastro().tipo_de_cadastro()