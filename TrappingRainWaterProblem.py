# water trapped between the blocks of the array is calculated using the below code snippet  
# The below code snippet is used to calculate the amount of water trapped between the blocks of the array.
# The input is taken from the user and the output is printed.
#https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?page=1&company=Amazon&sortBy=submissions&query=page1companyAmazonsortBysubmissions
#also print the left and right array to understand the code better 
#https://www.geeksforgeeks.org/trapping-rain-water/

def trap(): # function to calculate the amount of water trapped between the blocks of the array
    n = int(input()) # taking the input value of n
    arr = list(map(int, input().split())) # taking the input values of the array seperated by space
    left = [0] * n # list to store the left max of the array  we initialize it with 0 and the size of the list is n
    right = [0] * n # list to store the right max of the array we initialize it with 0 and the size of the list is n
    left[0] = arr[0]  # the first element of the left list is the first element of the array
    right[n-1] = arr[n-1] # the last element of the right list is the last element of the array
    for i in range(1, n): # for loop to calculate the left max of the array
        left[i] = max(left[i-1], arr[i]) # the left max of the array is the maximum of the previous element and the current element of the array
    for i in range(n-2, -1, -1): # for loop to calculate the right max of the array and  n-2 is the second last element of the array and -1 is the first element of the array
        right[i] = max(right[i+1], arr[i]) # the right max of the array is the maximum of the next element and the current element of the array
    #print(left)
    #print(right)    
    water = 0 # variable to store the amount of water trapped between the blocks of the array initialized with 0 
    for i in range(n): # for loop to calculate the amount of water trapped between the blocks of the array
        water += min(left[i], right[i]) - arr[i] # the amount of water trapped between the blocks of the array is the minimum of the left and right max of the array minus the current element of the array
    return water # returning the amount of water trapped between the blocks of the array

if __name__ == '__main__': 
    result = trap()
    print(result)
























