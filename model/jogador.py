from model.usuario import Usuario
from model.catalogo import Catalogo
from model.jogo import Jogo

class Jogador(Usuario):
    def __init__(self,tipo_de_usuario, nome_de_usuario: str, senha:str, genero:str, idade:int, biografia:str="Sem biografia ainda") -> None:
        super().__init__(tipo_de_usuario, nome_de_usuario, senha, biografia)
        self.__genero = None
        self.__idade = None
        self.__biblioteca_jogador = []

        if isinstance(genero, str):
            self.__genero = genero
        else:
            return "Genero incorreto"
        
        if isinstance(idade, int):
            self.__idade = idade
        else:
            return False
        
    def adquirir_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self.__biblioteca_jogador.append(jogo)
        else:
            return False
        
    def excluir_jogo(self,jogo):
        if isinstance(jogo, Jogo) and Jogo in self.__biblioteca_jogador:
            self.__biblioteca_jogador.remove(jogo)
        else:
            return False
        
    def lista_de_jogos(self):
        return self.__biblioteca_jogador
