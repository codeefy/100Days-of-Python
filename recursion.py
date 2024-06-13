# write a program using function which calculates the number of upper case
#letter lower case letter total number of characters and number of words .

def count_uppercase(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count
def count_lowercase(s):
    count=0
    for i in s :
        if i.islower():
            count+=1
    return count
def count




































def count_uppercase(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count
def count_lowercase(s):
    count=0
    for i in s:
        if i.islower():
            count+=1
    return count
def count_characters(s):
    count=0
    for i in s:
        count+=1
    return count
def count_words(s):
    count=0
    for i in s:
        if i==" ":
            count+=1
    return count+1 
def count_all(s):
    return count_uppercase(s),count_lowercase(s),count_characters(s),count_words(s)
s="FUNCTIONS have to be Defined before THEY can be called. the function Call Cannot come before the DEFINITION"
print(count_all(s))
 