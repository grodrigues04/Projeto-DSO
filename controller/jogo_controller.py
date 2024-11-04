from view.tela_jogo import TelaJogo
from model.jogo import Jogo
class JogoControler():
    def __init__(self, controlador_sistema) -> None:
        self.__tela_jogo = TelaJogo()
        self.__controlador_sistema = controlador_sistema
        self.__repositorio_de_jogos = []


    def adicionar_jogo(self, jogo_infos):
        novo_jogo = Jogo(jogo_infos["titulo"],
                    jogo_infos["autor"],
                    jogo_infos["genero"],
                    jogo_infos["armazenamento"],
                    jogo_infos["descricao"],
                    jogo_infos["idade_minima"]
                    )
        self.__repositorio_de_jogos.append(novo_jogo)

        #Adiciona o jogo que foi criado a biblioteca do objeto atual do DEV
        dev = self.__controlador_sistema.sessao_atual
        dev.adicionar_jogo(novo_jogo)

    def tela_de_criacao(self):
        dev_atual = self.__controlador_sistema.sessao_atual
        jogo_infos = self.__tela_jogo.criar_jogo(dev_atual)
        self.adicionar_jogo(jogo_infos)

    @property
    def repositorio_de_jogos(self):
        return self.__repositorio_de_jogos