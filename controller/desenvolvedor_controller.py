class DesenvolvedorController():
    def __init__(self, controlador_sistema) -> None:
        self.__devs = []
        self.__controlador_sistema = controlador_sistema

    @property
    def devs(self):
        return self.__devs
    
    def adicionar_dev(self, dev):
        self.__devs.append(dev)