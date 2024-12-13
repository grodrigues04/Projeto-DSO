class UsuarioRepetido(Exception):

    def __init__(self):
        super().__init__("Esse nome de usuario já existe")