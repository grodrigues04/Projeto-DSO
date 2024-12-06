from datetime import datetime
from .tela_abstrata import AbstractTela
class TelaCadastro(AbstractTela):
    def __init__(self) -> None:
        super().__init__()
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
        
        usuario_info = tipo_de_conta(login, senha, biografia, email)
        return usuario_info

    def cadastrarDev(self, login, senha, biografia, email):
        print("Você concorda com os termos [S/N] ?")
        termos = input().upper()
        # if termos == "N":
        #     print("Você não concordou com os termos, portan   to a conta não vai ser criada")
        #     return False
        print("Deseja criar sua biografia agora [S/N]?")
        usuario_info = {"tipo_de_conta":"desenvolvedor","nome_de_usuario":login, "biografia":biografia, "email":email, "termos":termos, "senha":senha}
        return usuario_info


    def cadastrarJogador(self, login, senha, biografia, email):
        ano_atual = datetime.now().year
        print("Qual seu Gênero? [M/F/OUTRO]")
        genero = input()
        print("Em que ano você nasceu ?")
        ano_nascido = int(input())
        idade = ano_atual - ano_nascido
        usuario_info = {"tipo_de_conta":"jogador","nome_de_usuario":login, "senha":senha,"genero":genero,"idade":idade,  "biografia":biografia}
        return usuario_info

    def tipo_de_cadastro(self):
        tipos_de_usuario = {1:self.cadastrarJogador, 2:self.cadastrarDev}
        saudacao_usuario = {1:"Jogador", 2:"Desenvolvedor"}
        print("Você quer criar uma conta de JOGADOR[1] ou DESENVOLVEDOR[2]")
        tipo_escolhido = self.le_num_inteiro("Escolha uma opcao", [1,2])
        return tipos_de_usuario[tipo_escolhido], saudacao_usuario[tipo_escolhido]