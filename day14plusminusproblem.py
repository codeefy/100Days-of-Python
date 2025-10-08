#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
#Print the decimal value of each fraction on a new line.
#Function description - Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
#plusMinus has the following parameter(s):
#   arr: an array of integers
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = sum(1 for i in arr if i > 0) /len(arr)
    negative = sum(1 for i in arr if i < 0) /len(arr)
    zero = sum(1 for i in arr if i == 0) /len(arr)
    return positive, negative, zero
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result=plusMinus(arr)

    print("{:,.6f}".format(result[0]))
    print("{:,.6f}".format(result[1]))
    print("{:,.6f}".format(result[2]))

