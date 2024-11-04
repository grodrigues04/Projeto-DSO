from model.jogador import Jogador
from model.desenvolvedor import Desenvolvedor
from view.tela_cadastro import TelaCadastro

class ControllerCadastro():
    def __init__(self, controlador_sistema) -> None:
        self.__tela_cadastro = TelaCadastro()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_usuario(self):
        tipos_de_usuario, saudacao = self.__tela_cadastro.tipo_de_cadastro()
        usuario_info = self.__tela_cadastro.cadastroGeral(tipos_de_usuario, saudacao)

        if usuario_info["tipo_de_conta"] == "jogador":
            jogador_control = self.__controlador_sistema.jogador_controler
            lista_jogadores = jogador_control.users
            jogador_existe = any(jogador.nome_de_usuario == usuario_info["nome_de_usuario"] for jogador in lista_jogadores)
            if not jogador_existe:
                novo_jogador = Jogador(
                    usuario_info["tipo_de_conta"],
                    usuario_info["nome_de_usuario"],
                    usuario_info["senha"],
                    usuario_info["genero"],
                    usuario_info["idade"],
                    usuario_info["biografia"]
                )
                jogador_control.adicionar_user(novo_jogador)
                return novo_jogador
            else:
                return False


        elif usuario_info["tipo_de_conta"] == "desenvolvedor":
            dev_control = self.__controlador_sistema.desenvolvedor_controler
            lista_devs = dev_control.users
            dev_existe = any(dev.nome_de_usuario == usuario_info["nome_de_usuario"] for dev in lista_devs)
            if not dev_existe:
                novo_dev = Desenvolvedor(
                    usuario_info["tipo_de_conta"],
                    usuario_info["nome_de_usuario"],
                    usuario_info["senha"],
                    usuario_info["email"],
                    usuario_info["termos"],
                    usuario_info["biografia"]
                )
                dev_control.adicionar_user(novo_dev)
                return novo_dev
            else:
                return False
        else:
            return None

    #@função_para_tela_De_acordo_com_o_usuario