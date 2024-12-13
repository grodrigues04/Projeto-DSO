from view.tela_jogador import TelaJogador
from .usuario_controller import UsuarioController
from DAOs.jogador_DAO import JogadorDAO
class JogadorController(UsuarioController): #TEM QUE TIRAR O SELF DO CONTROLADOR DO SISTEMA QUANDO INSTANCIA O JOGADOR CONTROLER
    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        #self.__jogadores = []
        self.__jogador_DAO = JogadorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()

    @property
    def users(self):
        #return self.__jogadores
        return self.__jogador_DAO.get_all()
    
    def adicionar_user(self, jogador):
        #self.__jogadores.append(jogador)
        self.__jogador_DAO.add(jogador)

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
                return "Idade mínima insuficiente"

        else:
            return "Sua biografia precisa de mais de 10 caracteres para poder adquirir um jogo"

    def biblioteca_do_jogador(self):
        sessao_atual = self.__controlador_sistema.sessao_atual
        jogos = sessao_atual.lista_de_jogos()
        self.__tela_jogador.mostrar_jogos(jogos)
    
    def iniciar_tela(self):
        window = self.__tela_jogador.configurar_tela()
        self.__controlador_sistema.adicionar_tela(window) #Adiciona a tela no histórico de telas
        info_tela = self.__tela_jogador.rodar(window)
        evento = info_tela["event"]

        if evento== "voltar":
            tela_anterior = self.__controlador_sistema.voltar_telas()
            #tela_anterior = self.__tela_jogador.voltar_tela()
            print("Tela anterior:", tela_anterior)
            self.__tela_jogador.abrir_tela(tela_anterior)
        if evento=="Comprar":
            pass
        elif evento=="Lista de jogos":
            self.__tela_jogador.configurar_get(self.biblioteca_do_dev())
