# water trapped between the blocks of the array is calculated using the below code snippet  
# The below code snippet is used to calculate the amount of water trapped between the blocks of the array.
# The input is taken from the user and the output is printed.
#https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?page=1&company=Amazon&sortBy=submissions&query=page1companyAmazonsortBysubmissions

def trap(): # function to calculate the amount of water trapped between the blocks of the array 
    n = int(input()) # taking the input value of n 
    arr = list(map(int, input().split())) # taking the input values of the array seperated by space 
    left = [0] * n # list to store the left max of the array  we initialize it with 0 and the size of the list is n
    right = [0] * n # list to store the right max of the array we initialize it with 0 and the size of the list is n
    left[0] = arr[0] # the first element of the left list is the first element of the array
    right[n-1] = arr[n-1]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - arr[i]
    return water

if __name__ == '__main__':
    result = trap()
    print(result) 
    # printing the output
