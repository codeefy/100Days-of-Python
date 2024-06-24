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
    alphabets = list(string.ascii_lowercase)
    rangoli = []
    for i in range(size):
        s = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])
        rangoli.append((s.center(size*4-3, '-')))
    print('\n'.join(rangoli[::-1] + rangoli[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

