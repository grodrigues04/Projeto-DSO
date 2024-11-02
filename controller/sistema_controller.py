from view.tela_sistema import TelaSistemaInicial
from .cadastro_controller import ControllerCadastro
from .login_controller import ControllerLogin
from .desenvolvedor_controller import DesenvolvedorController
from .jogador_controller import JogadorController

class ControladorSistema():
    def __init__(self) -> None:
        self.__tela_sistema = TelaSistemaInicial()
        self.__cadastro_controller = ControllerCadastro(self)
        self.__login_controller = ControllerLogin(self)
        self.__desenvolvedor_controller = DesenvolvedorController(self)
        self.__jogador_controller = JogadorController(self)
    @property
    def cadastro_controler(self):
        return self.__cadastro_controller
    
    def inicializa_sistema(self):
        self.abretela()

    #def abre_tela_inicial(self):
    def realizar_login(self):
        pass

    @property
    def login_controller(self):
        return self.__login_controller



    @property
    def desenvolvedor_controler(self):
        return self.__desenvolvedor_controller

    @property
    def jogador_controler(self):
        return self.__jogador_controller

    def cadastra_usuario(self):
        self.__cadastro_controller.cadastrar_usuario()