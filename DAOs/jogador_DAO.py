from DAOs.dao import DAO
from model.jogador import Jogador

#cada entidade terá uma classe dessa, implementação bem simples.
class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.nome, int)):
            super().add(jogador.nome, jogador)

    def update(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.nome, int)):
            super().update(jogador.nome, Jogador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)