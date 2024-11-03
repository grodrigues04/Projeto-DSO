from view.tela_login import TelaLogin
from .cadastro_controller import ControllerCadastro
# from .jogador_controller import JogadorController
# from .desenvolvedor_controller import DesenvolvedorController
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
            if usuario.nome_de_usuario == credenciais["nome_de_usuario"]: # Então realmente existe um usuario com esse nome
                print("Existe um usuario com esse nome de login")
                login_credenciais = usuario.fazer_login() #Retorna as credencias do usuario
                #nome_de_usuario_bd = login_credenciais["usuario"]
                senha_bd = login_credenciais["senha"]

                print(f"Nome de usuario do usuario.nome_de_usuario:{usuario.nome_de_usuario} | credenciais:{credenciais["nome_de_usuario"]}")
                print("Realmente existe um usuario que tem esse nome")
                if senha_bd == credenciais["senha"]:
                    print("Senha e nome de usuario corretos")
                    return True
                else:
                    print("Senha incorreta")
                    return "Senha errada, tente novamente."
            else:
                return "Usuario incorreto ou não existe. Tente novamente"
            
    def iniciar_login(self):
        usuario_credenciais = self.__tela_login.forms_login()
        status = self.verificar_credenciais(usuario_credenciais)
        while isinstance(status,str):
            self.__tela_login.mensagem(status)
            usuario_credenciais = self.__tela_login.forms_login()
        #INICIAR SISTEMA GLORIAAAAAAAAAAA
