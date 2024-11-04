from view.tela_login import TelaLogin
from .cadastro_controller import ControllerCadastro

class ControllerLogin():
    def __init__(self, controlador_sistema) -> None:
        self.__tela_login = TelaLogin()
        self.__controlador_sistema = controlador_sistema

    def verificar_credenciais(self, credenciais) -> bool:
        tipos_de_usuario = {1:self.__controlador_sistema.desenvolvedor_controler,
                            2:self.__controlador_sistema.jogador_controler 
                            }
        controler_de_verificacao = tipos_de_usuario[credenciais["tipo_de_conta"]]
        lista_de_usuarios = controler_de_verificacao.users

        for usuario in lista_de_usuarios:
            if usuario.nome_de_usuario == credenciais["nome_de_usuario"]:
                login_credenciais = usuario.fazer_login() 
                senha_bd = login_credenciais["senha"]
                if senha_bd == credenciais["senha"]:
                    return True, usuario, "Login bem sucedido. Entrando no sistema..."
                else:
                    return False,"Senha errada, tente novamente."
                
            return False,"Usuario incorreto ou não existe. Tente novamente"
            
    def iniciar_login(self):
        while True: #TODO: ESSE ISISTANCE AQUI TA HORRIVEL
            usuario_credenciais = self.__tela_login.forms_login()
            status, usuario, mensagem = self.verificar_credenciais(usuario_credenciais)
            print("print do usuario que ta chegando:",usuario)
            self.__controlador_sistema.sessao_atual = usuario
            self.__tela_login.mensagem(mensagem)
            if status:
                return usuario_credenciais["tipo_de_conta"]
