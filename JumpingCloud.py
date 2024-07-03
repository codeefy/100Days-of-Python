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
# In this problem, we are given an array c of integers where each element represents a cloud.
#  The value of each element can be 0 or 1. The value 0 represents a safe cloud, and the value 1 represents a thundercloud.
#  We have to find the minimum number of jumps required to reach the end of the array.
#  We can jump from one cloud to another if the difference between the indices of the two clouds is 1 or 2.
#  For example, if the array c is [0, 1, 0, 0, 0, 1, 0], then the minimum number of jumps required is 3.
#  The possible jumps are 0 -> 2 -> 3 -> 4 -> 6.
#  So, the output will be 3.
#  The idea is to start from the first cloud and check if we can jump 2 clouds ahead.
#  If we can jump 2 clouds ahead, then we jump 2 clouds ahead and call the function recursively with the remaining clouds.
#  If we cannot jump 2 clouds ahead, then we jump 1 cloud ahead and call the function recursively with the remaining clouds.
#  If we reach the end of the array, then we return 0.
#  If we reach the second last cloud, then we return 1.
#  If we reach the third last cloud, then we return 1.
#  If we reach the fourth last cloud, then we return 2.
#  If we reach the fifth last cloud, then we return 2.
#  If we reach the sixth last cloud, then we return 3.
#  If we reach the seventh last cloud, then we return 3.



def jumpingOnClouds(c): # Function to find the minimum number of jumps required to reach the end of the array 
    # Write your code here
    if len(c) == 1: # If we reach the end of the array, then we return 0 
        return 0 
    if len(c) == 2: # If we reach the second last cloud, then we return 1 
        return 1
    if c[2] != 1: # If we can jump 2 clouds ahead, then we jump 2 clouds ahead and call the function recursively with the remaining clouds
        return jumpingOnClouds(c[2:]) + 1  # If we cannot jump 2 clouds ahead, then we jump 1 cloud ahead and call the function recursively with the remaining clouds
    else: 
        return jumpingOnClouds(c[1:]) + 1

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

print(result)

#input :
# 7
# 0 0 1 0 0 1 0
#output:
# 4


   
