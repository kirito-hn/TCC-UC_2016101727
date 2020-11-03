
# -*- coding: utf-8 -*-

from os import path
import argparse
from arvoreh import ArvoreH
import pickle as pkl

parser = argparse.ArgumentParser('Algoritmo da Árvore de Huffman')
parser.add_argument('file', help='Arquivo de entrada', nargs='?', default=None)
parser.add_argument(
    'pickle_file', help='Arquivo com o objeto', nargs='?', default=None)
parser.add_argument(
    '-d', '--decode', help='Usado para realizar o decode', action='store_true')
args = parser.parse_args()


if __name__ == '__main__':
    try:
       
            # Entrada do texto
            while True:
                print("Digite o texto de entrada:")
                texto = input()

                if len(texto) > 0:
                    caracteres = list(texto)
                    arvore = ArvoreH()
                    arvore.add_texto(texto)
                    arvore.mount()
                    # exibe a entrada em codigo de huffman
                    code =  arvore.encode(texto)
                    print("entrada em codigo de huffman:",code,"\n")
                    # Traduz o codigo de huffman para o texto original
                    codex=arvore.decode(code)
                    print("codigo de huffman decodificado:", codex,"\n")
                    # exibe a arvore em pre ordem
                    print("Arvore de Huffman:")
                    arvore.preordem(arvore.raiz)
                    # exibe o dicionario
                    print("\n","\n","Dicionario:" ,arvore.dici)
                    # exibe o dicionario invertido
                    print("\n","\n","Dicionario invertido" ,arvore.reverso_dici)
                    
                    

                else:
                    raise EOFError
    except EOFError:
        pass
























