#Talvez, criar uma classe abstrata para controladores de usuarios
class DesenvolvedorController():
    def __init__(self, controlador_sistema) -> None:
        self.__devs = []
        self.__controlador_sistema = controlador_sistema

    @property
    def users(self):
        return self.__devs
    
    def adicionar_user(self, dev):
        self.__devs.append(dev)