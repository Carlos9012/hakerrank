import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
class editor:
    def __init__(self, palavra = [], desfazer = []):
        self.palavra = []
        self.desfaz = []

    def adicionar(self, string = ''):
        if self.palavra == []:
            self.desfaz = self.palavra
            palavra = ''.join(string)
            self.palavra = palavra
        else:
            self.desfaz = self.palavra
            res = self.palavra + string
            self.palavra = res
            
        return self.palavra

    def excluir(self, num = None):
        new_str = ""
        self.desfaz = self.palavra
        for i in range(len(self.palavra)): 
            if i != num-1: 
                new_str = new_str + self.palavra[i] 
        self.palavra = new_str
        return self.palavra

    def imprimir(self, num = None):
        string = '_' + self.palavra
        for i in range(0, len(string)):
            if i == num:
                return string[i]
    
    def desfazer(self):
        self.palavra = self.desfaz
        return self.palavra

if __name__ == '__main__':
    edit = editor()

    print(edit.adicionar('oi'))
    print(edit.excluir(1))
    #print(edit.imprimir(1))
    print(edit.adicionar('ol'))
    
    print(edit.desfazer())
    