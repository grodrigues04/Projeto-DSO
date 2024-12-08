from view.tela_jogador import TelaJogador
from .usuario_controller import UsuarioController
class JogadorController(UsuarioController): #TEM QUE TIRAR O SELF DO CONTROLADOR DO SISTEMA QUANDO INSTANCIA O JOGADOR CONTROLER
    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__jogadores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()

    @property
    def users(self):
        return self.__jogadores
    
    def adicionar_user(self, jogador):
        self.__jogadores.append(jogador)

    def perfil(self):
        self.__tela_jogador.alterar_perfil()

    def comprar_jogo(self):
        jogos_controler = self.__controlador_sistema.jogo_controler
        repositorio = jogos_controler.repositorio_de_jogos
        jogo_desejado = self.__tela_jogador.adquirir_jogo(repositorio)
        
        jogador_objeto = self.__controlador_sistema.sessao_atual
        biografia = jogador_objeto.biografia
        idade_minima = jogo_desejado.idade_minima
        if len(biografia) > 10:
            if idade_minima >= jogo_desejado.idade_minima:
                #Adiciona o jogo na biblioteca do objeto jogador e a lista de jogadores ativos do objeto Jogo
                jogador_objeto.adquirir_jogo(jogo_desejado)
                jogo_desejado.adicionar_jogador(jogador_objeto)
                self.iniciar_tela()
            else:
                return "Idade minima insuficiente"

        else:
            return "Sua biografia precisa de mais de 10 caracteres para poder adquirir um jogo"

    def biblioteca_do_jogador(self):
        sessao_atual = self.__controlador_sistema.sessao_atual
        jogos = sessao_atual.lista_de_jogos()
        self.__tela_jogador.mostrar_jogos(jogos)
    
    def iniciar_tela(self):
        while True: 
            acoes = {
                1: self.comprar_jogo,
                2: self.biblioteca_do_jogador,
                3: self.abrir_tela_de_perfil,
                4: self.sair,
                5: self.__controlador_sistema.tela_inicial
            }
            
            opcao = self.__tela_jogador.tela_opcoes()
            funcao = acoes[opcao]
            resposta = funcao()
            
            if isinstance(resposta,str):
                self.__tela_jogador.msg(resposta)  # Executa a função correspondente à opção escolhida
            
            if opcao == 4:  # Número correspondente à opção de sair
                break  # Encerra o loop para sair do menu
