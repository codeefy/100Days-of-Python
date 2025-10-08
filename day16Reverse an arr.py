#!/bin/python3
#https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true
# An array is a type of data structure that stores elements of the same type in a contiguous block of memory.

# In this challenge, you have to create an array of size  with the elements of being input from the user.
 
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip()) #take input from the user

    arr = list(map(int, input().rstrip().split()))#`split()` method splits a string into a list. You can specify the separator, default separator is any whitespace.
    reversed_A = arr[::-1] # for reversed arr list 
for num in reversed_A: #for each number in the reversed_A list
    print(num, end=' ') #print the number and add a space after each number 
   