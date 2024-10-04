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

    @jogos_disponiveis.setter
    def jogos_disponiveis(self, Jogo):
        guardar_jogo = [Jogo]
        self.__jogos_disponiveis.append(Jogo)
        return "Jogo adicionado com sucesso ao catalogo!"

    