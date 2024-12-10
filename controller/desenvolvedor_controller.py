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
        # dev_atual = sessao_atual.nome_de_usuario
        # jogos = self.__desenvolvedor_DAO.get(dev_atual).jogos_criados
        #print("os jogos que tao vindo do espacle", jogos)
        jogos = sessao_atual.jogos_criados
        biblioteca = []
        for jogo in jogos:
            print("Jogos na iteração o jogo:", jogo)
            biblioteca.append({"titulo":jogo["titulo"], "genero":jogo["genero"], "autor":jogo["autor"], "idade_minima":jogo["idade_minima"] })

        return biblioteca

    def criar_jogo(self):
        jogo_controler = self.__controlador_sistema.jogo_controler
        jogo_controler.tela_de_criacao()

    def iniciar_tela(self):
        info_tela = self.__tela_dev.rodar()
        evento = info_tela["event"]
        print("evento printado no controlador:", evento )
        if evento=="Criar jogo":
            pass
        elif evento=="Lista de jogos desenvolvidos":
            print(" EU TO ENTRANDO AQUI")
            self.__tela_dev.configurar_get(self.biblioteca_do_dev())