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

    def sair(self):
        exit(0)
        
    def iniciar_tela(self):
        while True:  # Loop para manter o usuário no menu até ele escolher sair
            acoes = {
                1: self.criar_jogo,
                2: self.biblioteca_do_dev,
                3: self.sair,
                4: self.__controlador_sistema.tela_inicial
            }
            
            opcao = self.__tela_dev.tela_opcoes()
            
            funcao = acoes.get(opcao)
            
            if funcao:
                funcao()  # Executa a função correspondente à opção escolhida
            else:
                print("Opção inválida. Tente novamente.")
            
            if opcao == 3:  # Número correspondente à opção de sair
                break  # Encerra o loop para sair do menue sair
