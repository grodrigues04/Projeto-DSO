class Catalogo():
    def __init__(self, jogos_disponiveis:list=[]) -> None:
        self.__jogos_disponiveis = []

    @property
    def jogos_disponiveis(self):
        return self.__jogos_disponiveis


    