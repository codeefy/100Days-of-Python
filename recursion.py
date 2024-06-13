# write a program using function which calculates the number of upper case
#letter lower case letter total number of characters and number of words .

"""def count_uppercase(s):
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
def count_characters(s):
    count=0
    for i in s :
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
print(count_all(s))"""

#write a python program using function to calculate area and perimeter of circle and rectangle. 
#input 'circle area 7' output 153.94 
#input 'rectangle area  15 10' output 150 
# exit output stop execution  
"""PI=22/7
def circle_area(r):
    return PI*r*r
def circle_perimeter(r):
    return 2*PI*r
def recangle_area(l,b):
    return l*b
def perimeter(l,b):
    return 2*(l+b)
while True:
    s=input().split()
    if s[0]=="circle":
        if s[1]=="area":
            print(circle_area(round(float(s[2]))))
        else:
            print(circle_perimeter(float(s[2])))
    elif s[0]=="rectangle":
        if s[1]=="area":
            print(recangle_area(float(s[2]),float(s[3])))
        else:
            print(perimeter(float(s[2]),float(s[3])))
    else:
        break"""

    #write a pyhton code using function which check whether the input 
    # cordinates for a triangle or not 
    #input (0,0),(0,1),(1,0) output yes
    #(2,3),(3,2),(2,3) output no 
    #(0,0),(10,0),(0,0.0001) output no

def check_triangle(x1,y1,x2,y2,x3,y3):
    if (x1==x2 and y1==y2) or (x2==x3 and y2==y3) or (x1==x3 and y1==y3):
        return "no"
    else:
        return "yes"
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
x3,y3=map(float,input().split())
print(check_triangle(x1,y1,x2,y2,x3,y3))

