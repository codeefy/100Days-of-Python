#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Complete the 'jumpingOnClouds' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.


def jumpingOnClouds(c):
    # Write your code here
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 1
    if c[2] != 1:
        return jumpingOnClouds(c[2:]) + 1
    else:
        return jumpingOnClouds(c[1:]) + 1

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

   
