# -*- coding: utf-8 -*-

class No():
              
    
    def __init__(self, label, values):
        self.label = label
        self.values = values
        self.direita = None
        self.esquerda = None

    def __repr__(self):
        return str((self.label, self.values, self.esquerda, self.direita))
































