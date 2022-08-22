#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    num = []
    for k in range(101):
        num.append(k)
    x =[]
    for g in range(100):
        x.append(0)
    
    y=[]
    for i in range(len(arr)):
        if arr[i] in num:
            x[arr[i]] = x[arr[i]]+1
    return x
    for j in range(len(x)):
        z =0
        while z<x[j]:
            y.append(num[j]-1)
            z+=1
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
