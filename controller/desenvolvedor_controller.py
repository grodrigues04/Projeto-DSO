#Talvez, criar uma classe abstrata para controladores de usuarios
from view.tela_dev import TelaDesenvolvedor
from .usuario_controller import UsuarioController
from DAOs.desenvolvedor_DAO import DesenvolvedorDAO

class DesenvolvedorController(UsuarioController):
    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        #self.__devs = []
        self.__desenvolvedor_DAO = DesenvolvedorDAO()

        self.__controlador_sistema = controlador_sistema
        self.__tela_dev = TelaDesenvolvedor()

    @property
    def users(self):
        print("O GET ALL:", self.__desenvolvedor_DAO.get_all() )
        return self.__desenvolvedor_DAO.get_all()
    
    def adicionar_user(self, dev):
        #self.__devs.append(dev)
        self.__desenvolvedor_DAO.add(dev)

    def compartilhar_jogo(self, jogo):
        catalago = self.__controlador_sistema.catalago_controler
        catalago.adicionar_jogo(jogo)

    def biblioteca_do_dev(self):
        sessao_atual = self.__controlador_sistema.sessao_atual
        jogos_criados = sessao_atual.jogos_criados
        self.__tela_dev.mostrar_jogos(jogos_criados)

    def criar_jogo(self):
        jogo_controler = self.__controlador_sistema.jogo_controler
        jogo_controler.tela_de_criacao()

    def iniciar_tela(self):
        while True:  # Loop para manter o usuário no menu até ele escolher sair
            acoes = {
                1: self.criar_jogo,
                2: self.biblioteca_do_dev,
                3: self.abrir_tela_de_perfil,
                4: self.sair,
                5: self.__controlador_sistema.tela_inicial
            }
            
            opcao = self.__tela_dev.tela_opcoes()
            
            funcao = acoes.get(opcao)
            
            if funcao:
                funcao()  # Executa a função correspondente à opção escolhida
            else:
                print("Opção inválida. Tente novamente.")
            
            if opcao == 3:  # Número correspondente à opção de sair
                break  # Encerra o loop para sair do menue sair
