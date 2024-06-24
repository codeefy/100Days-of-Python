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

#code starts here
def print_rangoli(size): 
    # your code here
    alphabets = list(string.ascii_lowercase) # list of alphabets from a to z in lowercase order
    rangoli = [] # list to store the alphabets in the rangoli pattern 
    for i in range(size): # for loop to iterate over the size of the rangoli pattern
        s = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size]) # joining the alphabets in the rangoli pattern with '-' 
        # and storing it in the variable s alphabets[size-1:i:-1] will give the alphabets in reverse order from the last alphabet to the ith alphabet 
        # and alphabets[i:size] will give the alphabets in the order from the ith alphabet to the last alphabet
        rangoli.append((s.center(size*4-3, '-'))) # appending the alphabets in the rangoli pattern to the list rangoli  center function will center the string s in the rangoli pattern
        # size*4-3 will give the length of the rangoli pattern  
    print('\n'.join(rangoli[::-1] + rangoli[1:])) # printing the rangoli pattern in the required format
    # rangoli[::-1] will give the alphabets in the reverse order and rangoli[1:] will give the alphabets in the order from the second element to the last element
    # join function will join the alphabets in the rangoli pattern with '\n' and print the output


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

