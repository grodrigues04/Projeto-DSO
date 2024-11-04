class Usuario():

    def __init__(self,tipo_de_usuario, nome_de_usuario:str, senha, biografia:str="Sem biografia ainda") -> None:
        
        self.__nome_de_usuario = None
        self.__senha = senha
        self.__tipo_de_usuario = None
        
        if isinstance(nome_de_usuario,str):
            self.__nome_de_usuario = nome_de_usuario
        else:
            return "Nome de usuario incorreto."

        self.__biografia = None
        if isinstance(biografia, str):
            self.__biografia = biografia
        
        if isinstance(tipo_de_usuario,str):
            self.__tipo_de_usuario = tipo_de_usuario
            

    def AlterarSenha(self,nova_senha):
        self.__senha = nova_senha
        return "Senha alterada com sucesso!"
    
    @property
    def tipo_de_usuario(self):
        return self.__tipo_de_usuario

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
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    def fazer_login(self):
        return {"usuario":self.__nome_de_usuario, "senha":self.__senha}
        
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
        
    