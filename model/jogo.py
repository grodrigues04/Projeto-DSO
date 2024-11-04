class Jogo():
    #inicializadores
    def __init__(self, titulo:str, autor:object, genero:str,armazenamento:str, biografia_jogo:str, idade_minima) -> None:
        #inicializa os atributos
        self.__armazenamento = armazenamento
        self.__autor = None
        self.__genero = None
        self.__biografia_jogo = None 
        self.__titulo = None
        self.__JogadoresAtivos = []
        self.__idade_minima = None
        #instancializa e verifica os tipos dos atributos que foram inicializados acima
        if isinstance(idade_minima, int):
            self.__idade_minima = idade_minima

        if isinstance(autor, object):
            self.__autor = autor
            
        if isinstance(genero, str):
            self.__genero = genero
            
        if isinstance(biografia_jogo, str):
            self.__biografia_jogo = biografia_jogo
            
        if isinstance(titulo, str):
            self.__titulo = titulo
                       
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self,autor):
        if isinstance(autor,str):
            self.__autor = autor
            return "Seu autor foi alterado!"
        else:
            return "Autor incorreto."

    @property
    def idade_minima(self):
        return self.__idade_minima

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self,genero):
        if isinstance(genero,str):
            self.__genero = genero
            return "O genero do jogo foi alterado!"
        else:
            return "Genero incorreto."

    @property
    def biografia_jogo(self):
        return self.__biografia_jogo

    @biografia_jogo.setter
    def biografia_jogo(self,biografia_jogo):
        if isinstance(biografia_jogo,str):
            self.__biografia_jogo = biografia_jogo
            return "A biografia do jogo foi alterada!"
        else:
            return "Biografia incorreta."
        
    #getter e setter de titulo
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        if isinstance(titulo,str):
            self.__titulo = titulo
            return "O titulo do jogo foi alterado!"
        else:
            return "titulo incorreto."
        
    @property
    def armazenamento(self):
        return self.__armazenamento

    
    #getter da lista de jogadores
    @property
    def JogadoresAtivos(self):
        return self.__JogadoresAtivos
    
    def adicionar_jogador(self,jogador):
        self.__JogadoresAtivos.append(jogador)

        #eu n sei se agente vai precisar de um setter pra lista de jogadore ativos, pq eu n botei setter no diagrama e n me lembro se precisava
        #mas por precaução, vou deixar o código pra adicionar jgoadores aqui, eu tb n sei se herdaremos da classe Jogador ou da classe Usuario
        #mas botei a classe Usuario pq acho que fica mais fácil de se localizar
        
        #def adicionar_jogador(self, usuario:nome_de_usuario):
            #if isinstance(usuario, nome_de_usuario):
                #self.__JogadoresAtivos.append(nome_de_usuario)
                #return "O jogador foi registrado com sucesso!"
           # else:
                #return "Invalido."

            
        
        
        
        
        
    