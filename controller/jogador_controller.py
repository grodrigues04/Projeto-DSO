from view.tela_jogador import TelaJogador
class JogadorController():
    def __init__(self, controlador_sistema) -> None:
        self.__jogadores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()

    @property
    def users(self):
        return self.__jogadores
    
    def adicionar_user(self, jogador):
        self.__jogadores.append(jogador)

    def comprar_jogo(self):
        pass

    def biblioteca_do_jogador(self):
        sessao_atual = self.__controlador_sistema.sessao_atual
        jogos = sessao_atual.lista_de_jogos()
        self.__tela_jogador.mostrar_jogos(jogos)
    
    def iniciar_tela(self):
        acoes = {
            1:self.comprar_jogo,
            2:self.biblioteca_do_jogador
        }
        opcao = self.__tela_jogador.tela_opcoes()
        funcao = acoes[opcao]
        funcao()