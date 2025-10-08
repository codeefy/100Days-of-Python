#write a factorial function using recursion
n=int(input())
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))

#First line: A word that starts with several Zs and continues by several Os.

#Note: The maximum length of this word must be 20

#You are required to enter a word that consists of  and 
#that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if Determine if the entered word is similar to word zoo.For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

#Print Yes if the entered word is similar to word zoo. Otherwise, print No.

#Input
#The input contains a word that consists of  and

#Output
#Print Yes if the entered word is similar to word zoo. Otherwise, print No.

#Example
#Input
#zzzoooooo
#Output
#Yes
n=(input())

def zoo(n):
    if n.count('z')*2==n.count('o'):
        return 'Yes'
    else:
        return 'No'

print(zoo(n))
#input:zzzoooooo
#output:Yes