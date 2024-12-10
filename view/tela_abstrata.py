from abc import ABC, abstractmethod
# import re
import PySimpleGUI as sg
# from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    def __init__(self):
        self.__ultima_tela = None

    @property
    def ultima_tela(self):
        return self.__ultima_tela
    
    @ultima_tela.setter
    def ultima_tela(self, nova_tela):
        self.__ultima_tela = nova_tela
    
    def exibir_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def configurar_get(self, lista):
        print("LISTA DO CONFIG DO GET",lista)
        if len(lista) >= 1:
            string = ""
            for dado in lista:
                print(dado)
                for chave, valor in dado.items():
                    if "-" in chave:
                        chave = chave.replace("-", " ")
                    string = string + f"{chave}: {valor}" + '\n' 
            self.exibir_mensagem(string)
        else:
            self.exibir_mensagem("Você ainda não desenvolveu nenhum jogo")

            

    @abstractmethod
    def configurar_tela():
        pass

    #Fica responsavel por abrir as telas
    def abrir_tela(self, window=None, condicao_especial=None, mensagem=None):
        self.__ultima_tela = window
        
        lista_de_eventos = ["ok","Criar jogo","Lista de jogos desenvolvidos","Editar Perfil",
                             "Encerrar Sistema","Tela inicial" ]
        
        while True:
            if mensagem:
                window["-MENSAGEM-"].update(mensagem)

            event, values = window.read()
            print(event)
            if event == sg.WIN_CLOSED or event in lista_de_eventos:
                break 

            if condicao_especial!=None:

                if condicao_especial=="password":
                    senha = values["senha_1"]
                    confirma_senha = values["senha_2"]
                    if senha != confirma_senha:
                        sg.popup("A senhas não conferem")
                    else:
                        break
                    
        window.close()
        print(event, values)
        return [event, values]

