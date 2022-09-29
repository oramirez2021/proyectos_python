#!/bin/python3

import math
import os
import random
import re
from operator import itemgetter


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input().strip())
    arr = sorted(arr,key=itemgetter(k))
    
    for i in range(0,n):
        texto = ""
        for j in range(0,m):
            texto = texto + " " + str(arr[i][j])
            if(j == 2):
                print(texto.strip(),end="\n")
    
