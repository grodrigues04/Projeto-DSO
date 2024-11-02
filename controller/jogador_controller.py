class JogadorController():
    def __init__(self,controlador_sistema) -> None:
        self.__jogadores = []
        self.__controlador_sistema = controlador_sistema

    @property
    def jogadores(self):
        return self.__jogadores
    
    def adicionar_jogador(self, jogador):
        self.__jogadores.append(jogador)