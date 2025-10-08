#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    frequency = {}
    count = 0
    
    # Count the frequency of each element
    for num in ar:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Count the number of pairs for each element
    for num, freq in frequency.items():
        if freq >= 2:
            count += freq // 2
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
