
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
        # verifica se é uma arquivo
        if args.file:
            with open(args.file, 'r') as in_file:
                texto = in_file.read()

                # verifica se é para realizar o decode
                if args.decode:
                    arvore = pkl.load(open(args.pickle_file, 'rb'))
                    print(arvore.decode(texto))

                else:
                    # realiza o encode do texto e salva o objeto
                    arvore = ArvoreH()
                    arvore.add_texto(texto)
                    arvore.mount()

                    print(arvore.encode(texto))

                    # salva o objeto
                    pkl.dump(arvore, open(
                        path.splitext(args.file)[-2] + '.code', 'wb'))
        else:
            # modo interativo
            while True:
                texto = input()

                if len(texto) > 0:
                    caracteres = list(texto)
                    arvore = ArvoreH()
                    arvore.add_texto(texto)
                    arvore.mount()
                    # print(Arvore.dici)
                    code =  arvore.encode(texto)
                    print(code)
                    # print(Arvore.decode(code))

                else:
                    raise EOFError
    except EOFError:
        pass
























