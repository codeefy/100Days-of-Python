"""import numpy 
#The first N line contains the integer .
N = int(input())

#The next  lines contains the  space separated elements of array .

arr = numpy.array([input().split() for _ in range(N)],float)

#print the determinant of arr
#2
#1.1 1.1
#1.1 1.1
print(round(numpy.linalg.det(arr), 2))

#Output
#0.0"""

import calendar
#print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

#A single line of input containing the space separated month, day and year, respectively, in MM DD year format.
#08 05 2015
#Output
#WEDNESDAY
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())  #calendar.day_name is used to get the name of the day of the week.
#calendar.weekday() is used to get the day of the week.
# .weekday() is used to get the day of the week.   
 # .upper() is used to convert the output to uppercase letters.

#3 captlize the first letter of each word in a string the string consists of alphanumeric characters and spaces.
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):  
    def capitalize_word(match): #capitalize_word is a function that takes a match object as an argument.
        word = match.group(0) #match.group(0) is used to get the matched string.
        if word[0].isdigit(): #isdigit() is used to check if the first character of the word is a digit.  
            return word  #If the first character is a digit, the word is returned as it is.
        else:
            return word.capitalize() #If the first character is not a digit, the word is capitalized.

    return re.sub(r'\b\w+\b', capitalize_word, s) #re.sub() is used to replace all the words in the string that match the pattern with the result of the capitalize_word function.  
    #\b is used to match the boundary of a word. 
    #\w+ is used to match one or more word characters.
    #\b is used to match the boundary of a word.
    #capitalize_word is used to capitalize the first letter of each word.
    #s is the input string.
    s=input()
    result = solve(s)
    print(result)
    
    