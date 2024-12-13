from abc import ABC, abstractmethod
# import re
import PySimpleGUI as sg
# from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    def __init__(self):
        self.__pilha_telas = []

    def fechar_tela(self, window):
        if window:
            window.close()

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

    # def voltar_tela(self):   
    #     print("TELAS:", self.__pilha_telas)
    #     if len(self.__pilha_telas) > 1:
    #         print("To caindo nesse")
    #         self.__pilha_telas.pop()  # Remove a tela atual
    #         return self.__pilha_telas[-1]  # Retorna a penúltima tela
    #     elif len(self.__pilha_telas) == 1:
    #         print("To caindo nesse if da funcao ?")
    #         return self.__pilha_telas[-1]  # Se for a única tela, retorna ela mesma
    #     return None  # Não há telas para voltar
    # #Fica responsável por abrir as telas
    
    def abrir_tela(self, window=None, condicao_especial=None, mensagem=None):
        # if len(self.__pilha_telas) == 0 or self.__pilha_telas[-1] != window:
        #     print("Adicionei uma tela...")
        #     self.__pilha_telas.append(window)  # Adiciona uma tela apenas se for nova
        #     print("Telas atuais:", self.__pilha_telas)
        
        lista_de_eventos = ["ok","Criar jogo","Lista de jogos desenvolvidos","Editar Perfil",
                             "Encerrar Sistema","Tela inicial", "voltar" ]
        
        while True:
            if mensagem:
                window["-MENSAGEM-"].update(mensagem)

            event, values = window.read()
            print("aqui que sai o print voltar",event)
            if event == sg.WIN_CLOSED or event in lista_de_eventos:
                break

            if event=="voltar":
                tela = self.voltar_tela()
                return tela


            if condicao_especial!=None:

                if condicao_especial=="password":
                    senha = values["senha_1"]
                    confirma_senha = values["senha_2"]
                    if senha != confirma_senha:
                        sg.popup("As senhas não conferem")
                    else:
                        break

        window.close()
        return [event, values]



