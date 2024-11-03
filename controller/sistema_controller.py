from view.tela_sistema import TelaSistemaInicial
from .cadastro_controller import ControllerCadastro
from .login_controller import ControllerLogin
from .desenvolvedor_controller import DesenvolvedorController
from .jogador_controller import JogadorController

class ControladorSistema():
    def __init__(self) -> None:
        self.__sessao_atual = None
        self.__tela_sistema = TelaSistemaInicial()
        self.__cadastro_controller = ControllerCadastro(self)
        self.__login_controller = ControllerLogin(self)
        self.__desenvolvedor_controller = DesenvolvedorController(self)
        self.__jogador_controller = JogadorController(self)
    @property
    def cadastro_controler(self):
        return self.__cadastro_controller
    

    #def abre_tela_inicial(self):
    def realizar_login(self):
        pass
    
    def comprar_jogo(self):
        pass

    @property
    def sessao_atual(self):
        return self.__sessao_atual

    @property
    def login_controller(self):
        return self.__login_controller

    @property
    def desenvolvedor_controler(self):
        return self.__desenvolvedor_controller

    @property
    def jogador_controler(self):
        return self.__jogador_controller
    
    def inicializa_sistema(self,sistema):
        tipos_de_tela = {
            2:self.__jogador_controller.iniciar_tela,
            1:self.__desenvolvedor_controller.iniciar_tela
        }
        #self.__tela_sistema.navegar_no_sistema()

        tela_do_usuario = tipos_de_tela[sistema]
        tela_do_usuario() #Chamando a tela de acordo com o tipo de usuario

    def cadastra_usuario(self):
        self.__sessao_atual = self.__cadastro_controller.cadastrar_usuario()
        print("sessao atual:", self.__sessao_atual.lista_de_jogos())
        tipo_de_conta = self.__login_controller.iniciar_login()
        self.inicializa_sistema(tipo_de_conta)


        #Talvez, a ordem em que as funções estão sendo chamadas é errada. Cadastro é uma função a parte. Deve haver uma outra função geral que contem uma lista de opções para iniciar o
        #sistema, onde o cadastro e uma das opcoes