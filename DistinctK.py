#Problem Statement
#You wish to help Ashish, who possesses a collection of N strings, 
# some of which may be duplicated, and has been assigned the task of finding the kth unique string.
#If the number of unique strings is less than k, he needs to display an empty string. 
# Considering you are Ashish's best friend can you assist him with this challenge?

#Input Format
#The first line contains an integer N denoting the number of strings.
#The next N lines contain strings.
#The next line contains an integer k.

#Output Format: The output contains the kth distinct string. If there are less than k unique string display an empty string.

#approach:
#1. Read the input values.
#2. Create a list to store the unique strings.
#3. Iterate through the list of strings.
#4. If the string is not in the list of unique strings, add it to the list.
#5. If the length of the list of unique strings is less than k, print an empty string.
#6. Otherwise, print the kth element of the list of unique strings.

#Example
#Input
#6
#d
#b
#c
#b
#c
#a
#2
#Output

# the answer is a as it is the 2nd distinct string in the list of strings and it comes first in the alphabetical order.
# Hence the output is a.
# write your code here
#input 
#3
#dac
#ba
#c
#1
#output
#dac because it is the 1st distinct string in the list of strings and it comes first in the alphabetical order. Hence the output is dac.
#but  the above code is not passing the test cases. So, I will modify the code to pass the test cases. 
#I will use the set() function to get the unique strings and then sort the unique strings and then print the kth element of the unique strings.
#I will modify the code as below
n = int(input())
strings = []
for i in range(n):
    strings.append(input())
k = int(input())
unique_strings = list(set(strings))
if len(unique_strings) < k:
    print("")
else:
    print(sorted(unique_strings)[k - 1])






    







