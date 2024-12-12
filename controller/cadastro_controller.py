from model.jogador import Jogador
from model.desenvolvedor import Desenvolvedor
from view.tela_cadastro import TelaCadastro

class ControllerCadastro:
    def __init__(self, controlador_sistema) -> None:
        self.__tela_cadastro = TelaCadastro()
        self.__controlador_sistema = controlador_sistema

    def abre_tela_cadastro(self, tipo_de_conta, mensagem=None):
        cadastro_info_view = self.__tela_cadastro.rodar(tipo_de_conta, mensagem)
        return cadastro_info_view[1]

    def cadastrar_usuario(self, tipo_de_conta):
        while True:
            usuario_info = self.abre_tela_cadastro(tipo_de_conta)

            if self.verifica_usuario_existe(tipo_de_conta, usuario_info["nome_de_usuario"]):
                self.__tela_cadastro.rodar(tipo_de_conta, "Erro: Nome de usuário já existe!")
            else:
                novo_usuario = self.criar_usuario(usuario_info, tipo_de_conta)
                self.__tela_cadastro.exibir_mensagem("Usuário cadastrado com sucesso!")
                return novo_usuario

    def verifica_usuario_existe(self, tipo_de_conta, nome_de_usuario):
        if tipo_de_conta == "jogador":
            lista_jogadores = self.__controlador_sistema.jogador_controler.users
            return any(jogador.nome_de_usuario == nome_de_usuario for jogador in lista_jogadores)
        elif tipo_de_conta == "desenvolvedor":
            lista_devs = self.__controlador_sistema.desenvolvedor_controler.users
            return any(dev.nome_de_usuario == nome_de_usuario for dev in lista_devs)
        return False

    def criar_usuario(self, usuario_info, tipo_de_conta):
        usuario_info["tipo_de_conta"] = tipo_de_conta
        if tipo_de_conta == "desenvolvedor":
            novo_dev = Desenvolvedor(
                usuario_info["tipo_de_conta"],
                usuario_info["nome_de_usuario"],
                usuario_info["senha_1"],
                usuario_info["email"],
                usuario_info["termos"],
                usuario_info["biografia"],
            )
            self.__controlador_sistema.desenvolvedor_controler.adicionar_user(novo_dev)
            return novo_dev

        elif tipo_de_conta == "jogador":
            novo_jogador = Jogador(
                usuario_info["tipo_de_conta"],
                usuario_info["nome_de_usuario"],
                usuario_info["senha_1"],
                usuario_info["genero"],
                usuario_info["idade"],
                usuario_info["biografia"],
            )
            self.__controlador_sistema.jogador_controler.adicionar_user(novo_jogador)
            return novo_jogador
