# birthday paradox problem using computational concept
import random
l=[]
#create an empty list

for i in range(30):
    l.append(random.randint(1,365))
    #add random numbers to the list between 1 and 365
    #append 30 of them 
l.sort()
print(l)
i=0
flag=0 #flag to check if there are any two same numbers or no repeatition
while(i<len(l)-1): # i<29 here we select up to 29 elements because we are comparing the current element with the next element
    if(l[i]==l[i+1]): #if the current element is equal to the next element
        print("Repeats",l[i],l[i+1]) #print the two elements
        flag=1 #set the flag to 1
        break #break the loop as we have found the two same elements
    i+=1 #increment i to check the next element
if(flag==0): #if flag is 0, then no repeats
    print("No repeats") #print no repeats