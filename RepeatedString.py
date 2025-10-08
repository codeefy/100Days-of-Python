# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# In this problem, we are given a string s and an integer n. We have to find the number of occurrences of 'a' in the string s repeated n times.
#  For example, if s = 'abcac' and n = 10, so the string will be abcacabcac.
#  The number of occurrences of 'a' in the new string is 4. So, the output will be 4.

# The idea is to find the number of occurrences of 'a' in the string s and then multiply it by 
# the number of times the string s is repeated in the new string.
#  If the length of the string s is less than n, then we need to find the number of occurrences of 'a' 
# in the string s and multiply it by the number of times the string s is repeated in the new string.
#  If the length of the string s is greater than n, then we need to find the number of occurrences of 'a'
#  in the first n characters of the string s.


def repeatedString(s, n):
    count = s.count('a') #count the number of 'a' in the string s
    length = len(s) #find the length of the string s
    repeat = n // length #find the number of times the string s is repeated in the new string
    remainder = n % length #find the number of characters left after repeating the string s
    result = count * repeat #find the number of occurrences of 'a' in the new string
    result += s[:remainder].count('a') #find the number of occurrences of 'a' in the remaining characters
    return result #return the result

s = input() #read the string s
n = int(input()) #read the integer n
result = repeatedString(s, n) #call the function repeatedString
print(result) #print the result

