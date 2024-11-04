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

        jogos_controler = self.__controlador_sistema.jogo_controler
        print(jogos_controler)
        repositorio = jogos_controler.repositorio_de_jogos
        print(repositorio)
        jogo_desejado = self.__tela_jogador.adquirir_jogo(repositorio)
        jogador_objeto = self.__controlador_sistema.sessao_atual
        biografia = jogador_objeto.biografia
        idade_minima = jogo_desejado.idade_minima
        if len(biografia) > 10:
            if idade_minima >= jogo_desejado.idade_minima:
                #Adiciona o jogo na biblioteca do objeto jogador e a lista de jogadores ativos do objeto Jogo
                jogador_objeto.adquirir_jogo(jogo_desejado)
                jogador_objeto.adicionar_jogador(jogador_objeto)
            else:
                return False, "Idade minima insuficiente"
        else:
            return False, "Sua biografia precisa de mais de 10 caracteres para poder adquirir um jogo"

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