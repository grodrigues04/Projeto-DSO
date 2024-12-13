class CamposVaziosException(Exception):
    def __init__(self):
        super().__init__("Todos os campos devem ser preenchidos.")
