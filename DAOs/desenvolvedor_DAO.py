from DAOs.dao import DAO
from model.desenvolvedor import Desenvolvedor

#cada entidade terá uma classe dessa, implementação bem simples.
class DesenvolvedorDAO(DAO):
    def __init__(self):
        super().__init__('desenvolvedor.pkl')

    def add(self, desenvolvedor: Desenvolvedor):
        if((desenvolvedor is not None) and isinstance(desenvolvedor, Desenvolvedor)) :
            super().add(desenvolvedor.nome_de_usuario, desenvolvedor)

    def update(self, desenvolvedor: Desenvolvedor):
        if((desenvolvedor is not None) and isinstance(desenvolvedor, Desenvolvedor)) :
            super().update(desenvolvedor.nome_de_usuario, Desenvolvedor)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)