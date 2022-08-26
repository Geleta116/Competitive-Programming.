#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    path.upper()
    current_pos = 0
    num_val = 0
    for i in range(len(path)):
        if path[i] == "U" and current_pos == -1:
                num_val +=1
                current_pos +=1
        elif path[i] == "U" and current_pos != -1:
            current_pos+=1
        elif path[i] == "D":
            current_pos -=1
    return(num_val)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
