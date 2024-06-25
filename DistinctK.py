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

#approach
#1. Read the input values
#2. Create a set to store the unique strings
#3. Iterate through the strings and add the strings to the set
#4. If the length of the set is less than k, print an empty string
#5. Else print the kth element of the set

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