# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true
# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the respective elements of the array.
from collections import Counter #import the Counter class from the collections module to count the frequency of elements in a list

import numpy as np
n=int(input().strip())
ar = list(map(int, input().rstrip().split()))
mean=print(np.mean(ar))
median=print(np.median(ar))
mode_counts = Counter(ar) #count the frequency of each element in the list and store it in a dictionary
max_count = max(mode_counts.values()) #get the maximum frequency of an element in the list 
modes = [k for k, v in mode_counts.items() if v == max_count] #get the element(s) with the maximum frequency in the list 
mode = min(modes) #get the smallest element with the maximum frequency in the list 

print( mode) #print the mode

    
    
