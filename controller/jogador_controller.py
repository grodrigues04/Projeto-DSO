class JogadorController():
    def __init__(self,controlador_sistema) -> None:
        self.__jogadores = []
        self.__controlador_sistema = controlador_sistema

    @property
    def users(self):
        return self.__jogadores
    
    def adicionar_user(self, jogador):
        self.__jogadores.append(jogador)