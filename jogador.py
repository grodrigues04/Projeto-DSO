from usuario import Usuario
from jogo import Jogo
class Jogador(Usuario):
    def __init__(self,nome_de_usuario: str, senha, genero:str, idade:int, biografia:str="Sem biografia ainda") -> None:
        super().__init__(nome_de_usuario, senha, biografia)
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
            return "Idade incorreta. Precisa ser um número inteiro"
        

    def adquirir_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self.__biblioteca_jogador.append(jogo)
        else:
            return "Adicionar o jogo na bibliteca falhou"
        
    def excluir_jogo(self,jogo):
        if isinstance(jogo, Jogo) and Jogo in self.__biblioteca_jogador:
            self.__biblioteca_jogador.remove(jogo)
        else:
            return "Retirar o jogo da biblitoeca falhou"
        
    def lista_de_jogos():
        pass