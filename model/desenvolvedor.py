from model.usuario import Usuario
from model.catalogo import Catalogo
from model.jogo import Jogo

class Desenvolvedor():
    def __init__(self, jogo:Jogo, titulo:str,  nome_de_usuario: str, senha:str, email:str, idade:int, termos_condicoes:bool, jogos_disponiveis:list, biografia:str="Sem biografia ainda") -> None:
        super().__init__(nome_de_usuario, senha, biografia, jogos_disponiveis, titulo)
        self.__email = None
        self.__termos_condicoes = None
        self.__jogo = None

        if isinstance(jogo, Jogo):
            self.__jogo = Jogo
        else:
            return "Jogo Incorreto"

        if isinstance(email, str):
            self.__email = email
        else:
            return "Email incorreto"
        
        if isinstance(termos_condicoes, bool):
            self.__termos_condicoes = termos_condicoes
        else:
            return "Termos e condições incorreto."

    @property  
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email
            return "Seu email foi alterado!"
        else:
            return "Insira um email válido."
    
    def checar_termos(self, termos_condicoes):
        if termos_condicoes:
            return "Termos e condições aceitados com sucesso!"
        else:
            return "Termos e condições não foram concordados."
    
    def checar_senha(self, senha):
        if len(senha) < 10:
            print("Insira uma senha válida.")
            return False
        else:
            print("Senha aceita com sucesso!")
            return True
        
    def compartilhar_jogo(self, jogo):
        jogo_adicionar = [jogo]
        self.__jogos_disponiveis.append(jogo_adicionar)
        return "Seu jogo foi compartilhado com sucesso!"
    
    def excluir_jogo(self, titulo):
        for jogo_atual in self.__jogos_disponiveis:
            if jogo_atual[0] == titulo:
                self.__jogos_disponiveis.remove(jogo_atual)
                return "Seu jogo foi excluido com sucesso!"


            

        


