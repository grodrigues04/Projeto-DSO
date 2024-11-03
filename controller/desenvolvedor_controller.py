#Talvez, criar uma classe abstrata para controladores de usuarios
from view.tela_dev import TelaDesenvolvedor
class DesenvolvedorController():
    def __init__(self, controlador_sistema) -> None:
        self.__devs = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_dev = TelaDesenvolvedor()

    @property
    def users(self):
        return self.__devs
    
    def adicionar_user(self, dev):
        self.__devs.append(dev)

    def iniciar_tela(self):
        self.__tela_jogador.tela_opcoes()

    def compartilhar_jogo(self):
        pass

    def biblioteca_do_dev(self):
        sessao_atual = self.__controlador_sistema.sessao_atual
        jogos_criados = sessao_atual.jogos_criados
        self.__tela_dev.mostrar_jogos(jogos_criados)

    def iniciar_tela(self):
        acoes = {
            1:self.compartilhar_jogo,
            2:self.biblioteca_do_dev
        }
        opcao = self.__tela_dev.tela_opcoes()
        funcao = acoes[opcao]
        funcao()