from model.jogador import Jogador
from model.desenvolvedor import Desenvolvedor

class Login():
    def verificar_credenciais(self) -> bool:
        pass

class Cadastro():
    def __init__(self) -> None:
        self.__desenvolvedores = []
        self.__jogadores = []
    def cadastrar_usuario(self, tipo_usuario, usuario_info):
        if tipo_usuario == "jogador":
            novo_jogador = Jogador(usuario_info["nome_de_usuario"], usuario_info["senha"], usuario_info["genero"], usuario_info["idade"], usuario_info["biografia"] )
            self.__desenvolvedores.append(novo_jogador)
        elif tipo_usuario == "desenvolvedor":
            novo_dev = Desenvolvedor(usuario_info["nome_de_usuario"], usuario_info["senha"],usuario_info["email"], usuario_info["termos"], usuario_info["biografia"])
            self.__desenvolvedores.append(novo_dev)
        else:
            print("Tipo de usuário inválido.")
            return None    
        print(f"lista dev: {self.__desenvolvedores} lista jog: {self.__jogadores}")

    #@função_para_tela_De_acordo_com_o_usuario