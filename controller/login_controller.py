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
                    self.__tela_login.exibir_mensagem("Senha errada. Tente novamente")
                    return False, None,"Senha errada, tente novamente."
            else:
                continue

        self.__tela_login.exibir_mensagem("Usuario incorreto ou não existe. Tente novamente")
        return False, None, "Usuario incorreto ou não existe. Tente novamente"
            
    def iniciar_login(self, tipo_de_conta):
        conta = {"desenvolvedor":1, "jogador":2}
        
        while True: 
            #usuario_credenciais = self.__tela_login.rodar(tipo_de_conta)
            window = self.__tela_login.configurar_tela(tipo_de_conta)
            self.__controlador_sistema.adicionar_tela(window)
            usuario_credenciais = self.__tela_login.rodar(window,tipo_de_conta)
            usuario_credenciais = {
                "nome_de_usuario":usuario_credenciais["values"][0],
                "senha":usuario_credenciais["values"][1],
                "tipo_de_conta": conta[tipo_de_conta]
            }

            status, usuario, mensagem = self.verificar_credenciais(usuario_credenciais)
            self.__controlador_sistema.sessao_atual = usuario
            self.__tela_login.mensagem(mensagem)
            if status:
                return usuario_credenciais["tipo_de_conta"]
