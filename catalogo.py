from jogo import Jogo

class Catalogo():
    def __init__(self, jogo: Jogo, jogos_disponiveis:list=[]) -> None:
        self.__jogos_disponiveis = []
        self.__jogo = None

        if isinstance(jogo, Jogo):
            self.__jogo = Jogo

    @property
    def jogos_disponiveis(self):
        return self.__jogos_disponiveis


    