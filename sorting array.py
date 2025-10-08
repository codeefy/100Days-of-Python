#we just learn that breaking our problem into smaller modules and solving them 
#makes it easy on our mind. 
#method 2 that is used for best and fast result 
def min_list(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini=l[i]
    return mini
def obvious_sort1(l):
    x=[]
    while len(l)>0:
        mini=min_list(l)
        x.append(mini)
        l.remove(mini)
    return x 
l=[20,30,11,5,2,3,-3,2]
l=[20,30,11,5,2,3,-3,2]
print(min_list(l)) #it gives the minimum value from the list 
print(obvious_sort1(l))