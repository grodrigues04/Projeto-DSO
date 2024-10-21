class Usuario():

    def __init__(self, nome_de_usuario:str, senha, biografia:str="Sem biografia ainda") -> None:
        
        self.__nome_de_usuario = None
        self.__senha = senha
        
        if isinstance(nome_de_usuario,str):
            self.__nome_de_usuario = nome_de_usuario
        else:
            return "Nome de usuario incorreto."

        self.__biografia = None
        if isinstance(biografia, str):
            self.__biografia = biografia
            
            

    def AlterarSenha(self,nova_senha):
        self.__senha = nova_senha
        return "Senha alterada com sucesso!"
    
    @property
    def nome_de_usuario(self):
        return self.__nome_de_usuario

    @nome_de_usuario.setter
    def nome_de_usuario(self,novo_usuario):
        if isinstance(novo_usuario,str):
            self.__nome_de_usuario = novo_usuario
            return "Seu nome de usuario foi alterado!"
        else:
            return "Nome de usuario incorreto."
        
    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self,nova_biografia):
        if isinstance(nova_biografia,str):
            self.__biografia = nova_biografia
            return "Sua biografia foi alterada com sucesso!"
        else:
            return "Biografia incorreta."
        
    