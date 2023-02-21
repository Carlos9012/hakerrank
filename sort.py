import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
#mais menos
def counting(dados):
    valores = []
    aux = ""
    cont = 0
    repetidos = set()
    
    for dado in dados:
        if dado not in valores:
            valores.append(dado)
        else:
            repetidos.add(dado)
    print(f'Valores = {valores}')
    print(f'Repetidos = {repetidos}')
    valores.sort()

    for i in repetidos:
        if i != valores[cont]:
            aux = i
            break
        cont+=1
    
    if aux == "":
        aux = valores[len(valores) - 1]
    
    return aux
    



if __name__ == '__main__':
    arr = [1,2,3,4,3,2,1]
    print(counting(arr))