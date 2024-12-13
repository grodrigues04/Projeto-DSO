class IntException(Exception):

    def __init__(self):
        super().__init__("Digite um valor inteiro")