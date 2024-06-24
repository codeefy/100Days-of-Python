# You are given an integer,Your task is to print an alphabet rangoli of size 
# N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:
# size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#approach:
# 1. First we need to create a list of alphabets from a to z.
# 2. Then we need to create a list of alphabets from a to z in reverse order.


import string # importing the string module from python for the list of alphabets from a to z in lower case
def print_rangoli(size): # function to print the rangoli of alphabets
    alphabets = string.ascii_lowercase # list of alphabets from a to z  in lower case 
    n = size # size of the rangoli 
    x = list(range(n)) # list of numbers from 0 to n-1  
    x = x[:-1]+x[::-1] # list of alphabets from a to z in reverse order x[:-1] is used to remove the last element from the list x[::-1] is used to reverse the list x
    for i in x:
        print('-'.join(alphabets[n-1:i:-1]+alphabets[i:n]).center(n*4-3, '-')) # printing the alphabets in the required format using join and center function of python 

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)