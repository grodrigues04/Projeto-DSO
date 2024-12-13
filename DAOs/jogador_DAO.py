from DAOs.dao import DAO
from model.jogador import Jogador

#cada entidade terá uma classe dessa, implementação bem simples.
class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador):
        if(jogador is not None) and isinstance(jogador, Jogador):
            super().add(jogador.nome_de_usuario, jogador)

    def update(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador)):
            super().update(jogador.nome_de_usuario, Jogador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)