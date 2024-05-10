l=[12,22,33,44,11,2,4,6,7,8,99,234,56,76,89] #create a list of numbers
#l.sort()# not use this write basic code to sort the list
x=[] #create an empty list to store the sorted list
while(len(l)>0): #while the length of the list is greater than 0 
    min=l[0]#initialize min to the first element of the list
    for i in range(len(l)): # for i in the range of the length of the list 
        if l[i]<min: #if the current element is less than the min
            min=l[i] #set the min to the current element 
    x.append(min) #append the min to the new list
    l.remove(min) #remove the min from the original list
print(l) #print the original list
print(x) #print the sorted list