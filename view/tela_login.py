#Essa tela tem que ser chamada apos o cadastro, 
#E apos o login, chamar a tela que varia de acordo com a entidade(jogador,dev) com as opções de navegação
from .tela_abstrata import AbstractTela
class TelaLogin(AbstractTela):

    def __init__(self) -> None:
        super().__init__()

    def mensagem(self,mensagem):
        print(mensagem)

    def forms_login(self):
        #Tem que mudar essa merda aqui pra ficar pedindo login e senha ate o usuario entrar
        print()
        print(" --- STEAM DOIS ---")
        print("Em qual conta você você quer entrar? [DESENVOLVEDOR(1)|JOGADOR(2)]")
        while True:
            tipo_de_conta = self.le_num_inteiro("Escolha uma opcao", [1,2])
            print("Digite seu nome de usuario")
            nome_de_usuario = input()
            print("Digite sua senha")
            senha = input()
            print()
            return {"tipo_de_conta":tipo_de_conta,
                    "nome_de_usuario":nome_de_usuario,
                    "senha":senha}