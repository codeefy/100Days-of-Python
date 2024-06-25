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
#a 
