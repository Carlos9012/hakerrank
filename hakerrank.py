import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result

def cont(arr):
    pos = 0
    neg = 0
    zer = 0
    result_pos = 0
    result_neg = 0
    result_zer = 0

    round(result_zer, 6)
    
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        elif i == 0:
            zer+=1

    result_neg = neg / len(arr)
    result_pos = pos / len(arr)
    result_zer = zer / len(arr)
    
    print("{:.6f}".format(result_pos))
    print("{:.6f}".format(result_neg))
    print("{:.6f}".format(result_zer))
    return

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    cont(arr)