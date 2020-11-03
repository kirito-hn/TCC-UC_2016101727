# -*- coding: utf-8 -*-
from no import No
from collections import Counter

class ArvoreH():
    
    '''
        Classe com a Árvore de Huffman

        attr:
            no(No[]): lista de nós
            raiz(No): nó raíz
            dici(dici): dicionário com os códigos
            reverso_dici(dici): dicionário invertido
    '''

    def __init__(self):
        '''
            Construtor
        '''
        self.nos = []
        self.raiz = None
        self.dici = {}
        self.reverso_dici = {}

    def add_texto(self, text):
        count = Counter(list(text))
        for key in count:
            self.add_no(No(key, count[key]))

    def add_no(self, no):
        '''
            Adiciona um nó na lista

            params:
                no(No): novo nó a ser adicionado
        '''
        self.nos.append(no)
         
        # ordena inversamente pelo valor do nó
        self.nos.sort(key=lambda x: x.values, reverse=True)

    def mount(self):
        '''
            Constrói a Árvore de Huffman
        '''
        while len(self.nos) > 1:

            # pegar nó da esquerda e direita
            # que são os dois úlitmos da lista
            no_esquerda = self.nos[-2]
            no_direita = self.nos[-1]

            # novo nó que será o pai dos dois anteriores
            no = No(no_esquerda.label + no_direita.label,
                        no_esquerda.values + no_direita.values)

            # atribuir os nós filhos ao pai
            no.esquerda = no_esquerda
            no.direita = no_direita

            # remover os dois último nós
            self.nos = self.nos[:-2]

            # adicionar o novo nó
            self.add_no(no)

        # salva a raiz
        self.raiz = self.nos[0]

        # criar o dicionário das letras
        self.__mount_dici()

        # criar dicionário invertido
        self.__reverso_dici()

    def __mount_dici(self):
        '''
            Cria o dicionário das letras com
            o repectivo código
        '''
        self.__nav_arvore(self.raiz, '')

    def __nav_arvore(self, no, code):
        '''
            Navega pela ávore e adiciona o código ao dicionário
        '''

        # se for um nó folha
        if no.esquerda == no.direita:
            self.dici[no.label] = code
        else:

            # olhar nó da esquerda
            if no.esquerda:
                self.__nav_arvore(no.esquerda, code + '0')

            # olhar nó da direita
            if no.direita:
                self.__nav_arvore(no.direita, code + '1')

    def __reverso_dici(self):
        '''
            Cria o dicionário revertido
        '''
        self.reverso_dici = {self.dici[Key]: Key for Key in self.dici}

    def encode(self, text):
        '''
            Realiza o encode em um texto, usando o dicionário criado

            params:
                text(str): texto original
        '''
        result = ''

        for letter in list(text):

            # verifica se a letra está no dicionário
            if self.dici.get(letter):
                result += self.dici[letter]
            else:
                result += '?'

        return result

    def decode(self, code):
        '''
            Decodificar o códido em texto

            params:
                code(str): código
        '''
        result = ''
        acc = ''

        code = [c for c in code if c.isdigit()]

        for number in code:
            acc += number

            # verifica se está no dicionário
            if self.reverso_dici.get(acc):
                result += self.reverso_dici[acc]
                acc = ''
                
        return result
   
    


    def preordem (self,no):
       # exibi a arvore de huffman em pré-ordem.
       if (no):
           print("{",no.values, end="")
           self.preordem(no.esquerda)
           self.preordem(no.direita)
           print("}",end="")  
       
   
    
                
                   
            
            
            
             
               
              
                
          
                
                
                
            
            
   
        
