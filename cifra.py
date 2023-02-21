import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    new_data = ''
    for c in data:
        index = alfabeto.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alfabeto)
            new_data += alfabeto[new_index:new_index+1]
    return new_data

# Tests
if __name__ == '__main__':
    key = 3
    original = 'there´s-a-starman-waiting-in-the-sky'
    print('  Original:', original)
    ciphered = caesar(original, key, MODE_ENCRYPT)
    print('Encriptada:', ciphered)
    plain = caesar(ciphered, key, MODE_DECRYPT)
    print('Decriptada:', plain)