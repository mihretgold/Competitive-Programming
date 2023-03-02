#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def sumSuperDigit(string):
    if len(string) == 1:
        return int(string)
    sums = 0.0
    for num in string:
        sums += int(num)
    
    
    return sumSuperDigit(str(int(sums)))
    
def superDigit(n, k):
    string = ""
    
    ans = sumSuperDigit(n)
    total = 0
    for index in range(k):
        total += int(ans)
    string = str(total)
    
    
    return sumSuperDigit(string)   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
