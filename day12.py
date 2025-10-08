# Description: This file contains the solution to the problem of finding the sum of the elements in a list
arr=[2,3,4,5,5,6]
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)


sum=0 #initialize sum to 0 to store the sum of the elements
ar_count = int(input().strip()) #get the number of elements in the list 
ar = list(map(int, input().rstrip().split())) #get the elements of the list and store it in a list called ar 
for i in range(len(ar)): #for i in the range of the length of the list 
    sum=sum+ar[i] #add the elements of the list to the sum

print(sum)    #print the sum
    
