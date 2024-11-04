from view.tela_perfil import TelaPerfil

class UsuarioController():

    def sair(self):
        exit()
        
    def __init__(self, controlador_sistema) -> None:
        self.__tela_perfil = TelaPerfil()
        self.__controlador_sistema = controlador_sistema

    def lista_de_usuario(self):
        if self.controlador_sistema.sessao_atual.tipo_de_usuario == "desenvolvedor":
            usuario_control = self.__controlador_sistema.desenvolvedor_controler
        else:
            usuario_control = self.__controlador_sistema.jogador_controler
        contas_de_usuario = usuario_control.users
        return contas_de_usuario
    
    def mudar_nome_de_usuario(self, novo_nome):
        lista_de_usuarios = self.lista_de_usuario()
        for usuario in lista_de_usuarios:
            if usuario.nome_de_usuario == novo_nome:
                return False, "Nome de usuário já existe. Por favor, escolha outro nome."

        self.controlador_sistema.sessao_atual.nome_de_usuario = novo_nome
        print("Nome de usuário alterado com sucesso!")
        return True, "Nome de usuario alterado!"  # Indica que a mudança de nome foi bem-sucedida
    
    def mudar_senha(self):

        senha_bd = self.__controlador_sistema.sessao_atual.senha
        while True:
            credenciais = self.__tela_perfil.mudar_senha()
            if credenciais["senha_atual"] == senha_bd:
                self.__controlador_sistema.sessao_atual.senha = credenciais["nova_senha"]
                self.__tela_perfil.msg("Sua senha foi alterada com sucesso. Faça login novamente")
                self.__controlador_sistema.tela_inicial()

            else:
                self.__tela_perfil.msg("Sua senha atual está incorreta")


        
    def mudar_biografia(self):
        pass

    def abrir_tela_de_perfil(self):
        opcao = self.__tela_perfil.tela_opcoes()
        funcoes = {
            1:self.mudar_nome_de_usuario,
            2:self.mudar_senha,
            3:self.mudar_biografia
        }
        funcao = funcoes[opcao]
        funcao()