from .tela_abstrata import AbstractTela
class TelaSistemaInicial(AbstractTela):
    def __init__(self) -> None:
        super().__init__()
    def navegar_no_sistema(self):
        print()
        print("-------- Steam 2 ---------")
        print("Escolha sua opcao")
        print("1 - Fazer login")
        print("2 - Realizar Cadastro")
        print("3 - Sair ")
        opcao = self.le_num_inteiro("Escolha a opcao:", [1,2,3])
        print("-------- Steam 2 ---------")
        print()
        return opcao
    