from view.tela_sistema import TelaSistemaInicial
from .cadastro_controller import ControllerCadastro
from .login_controller import ControllerLogin
from .desenvolvedor_controller import DesenvolvedorController
from .jogador_controller import JogadorController
from .jogo_controller import JogoControler
from .usuario_controller import UsuarioController
class ControladorSistema():
    def __init__(self) -> None:
        self.__sessao_atual = None
        self.__tela_sistema = TelaSistemaInicial()
        self.__cadastro_controller = ControllerCadastro(self)
        self.__login_controller = ControllerLogin(self)
        self.__desenvolvedor_controller = DesenvolvedorController(self)
        self.__jogador_controller = JogadorController(self)
        self.__jogo_controller = JogoControler(self)
        self.__usuario_controller = UsuarioController(self)
        self.__pilha_telas = []

    @property
    def cadastro_controler(self):
        return self.__cadastro_controller
    
    @property
    def usuario_controler(self):
        return self.__usuario_controller

    @property
    def jogo_controler(self):
        return self.__jogo_controller

    def adicionar_tela(self, window):
        if len(self.__pilha_telas) == 0 or self.__pilha_telas[-1] != window:
            print("Adicionei uma tela...")
            self.__pilha_telas.append(window)  # Adiciona uma tela apenas se for nova
            print("Telas atuais:", self.__pilha_telas)
        self.__pilha_telas

    def voltar_telas(self):
        print("TELAS:", self.__pilha_telas)
        if len(self.__pilha_telas) > 1:
            print("To caindo nesse")
            ultima_tela = self.__pilha_telas.pop()  # Remove a tela atual
            self.__tela_sistema.fechar_tela(ultima_tela)
            return self.__pilha_telas[-1]  # Retorna a penúltima tela
        elif len(self.__pilha_telas) == 1:
            print("To caindo nesse if da funcao ?")
            return self.__pilha_telas[-1]  # Se for a única tela, retorna ela mesma
        return None  # Não há telas para voltar
    #Fica responsável por abrir as telas  

    #def abre_tela_inicial(self):
    def realizar_login(self, tipo_de_conta):
        tipo_de_conta = self.__login_controller.iniciar_login(tipo_de_conta)
        self.inicializa_sistema(tipo_de_conta)
    
    def comprar_jogo(self):
        pass

    @property
    def sessao_atual(self): #pega a conta atual que esta usando o sistema. Mais especificamente o objeto.
        return self.__sessao_atual

    @sessao_atual.setter
    def sessao_atual(self, nova_sessao):
        self.__sessao_atual = nova_sessao

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

    def cadastra_usuario(self, tipo_de_conta):
        self.__sessao_atual = self.__cadastro_controller.cadastrar_usuario(tipo_de_conta)
        tipo_de_conta = self.__login_controller.iniciar_login(tipo_de_conta)
        self.inicializa_sistema(tipo_de_conta)

    def opção_escolhida(self, event, values):
        if event!= None:
            for key in [1, 2]:
                if values[key]:  # Verifica se o valor é True
                    ação_escolhida = key
                    break   
            for key in ['desenvolvedor', 'jogador']:
                if values[key]:  # Verifica se o valor é True
                    tipo_de_conta = key
                    break
            return[ação_escolhida, tipo_de_conta]

    def tela_inicial(self):
        opcao = self.__tela_sistema.rodar()
        opcao = self.opção_escolhida(opcao[0], opcao[1])
        if opcao:
            opcoes_de_tela = {
                1:self.realizar_login,
                2:self.cadastra_usuario,
            }
            funcao = opcoes_de_tela.get(opcao[0]) #Pegando a ação escolhida do return da função
            if funcao:
                funcao(opcao[1])  #qual o tipo de conta
            else:
                print("Opção inválida. Tente novamente.")