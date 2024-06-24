import string

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

"""
import string # importing the string module from python for the list of alphabets from a to z in lower case
def print_rangoli(size): # function to print the rangoli of alphabets
    alphabets = string.ascii_lowercase # list of alphabets from a to z  in lower case 
    n = size # size of the rangoli 
    x = list(range(n)) # list of numbers from 0 to n-1  
    x = x[:-1]+x[::-1] # list of alphabets from a to z in reverse order x[:-1] is used to remove the last element from the list x[::-1] is used to reverse the list x
    for i in x: # for loop to print the alphabets in the required format 
        print('-'.join(alphabets[n-1:i:-1]+alphabets[i:n]).center(n*4-3, '-')) # printing the alphabets in the required format using join and center function of python  
        # alphabet[n-1:i:-1] is used to print the alphabets in reverse order from n-1 to i alphabet[i:n] is used to print the alphabets from i to n .center(n*4-3, '-') 
        # is used to center the alphabets in the required format

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
#input: 5"""
#output:
#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------
# but the code is not working as expected. It is giving the output as:
"""e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e"""
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    n = size
    x = list(range(n))
    x = x[:-1]+x[::-1]
    for i in x:
        pattern = '-'.join(alphabets[n-1:i:-1]+alphabets[i:n])
        print(pattern.center(n*4-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)