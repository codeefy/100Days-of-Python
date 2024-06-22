# Link: https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
# Title: Trapping Rain Water


# Trapping Rain Water
# Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
# Example 1:
# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output:
# 10
# Explanation: The heights are 3 0 0 2 0 4. So we can trap "3*2 units of water" between the 3 and 2, "1 unit" between the 2 and 0 and "3 units" between the 2 and 4. Hence, the total unit of water trapped is 10.

class Solution: # class to calculate the amount of water trapped between the blocks of the array 
    def trappingWater(self, arr, n): # function to calculate the amount of water trapped between the blocks of the array
        # Two-pointer approach is used to solve the problem 
        # two pointer approach is like a sliding window approach where we use two pointers to traverse the array 
        # where one pointer is at the start of the array and the other pointer is at the end of the array and 
        # we use these pointers to calculate the amount of water trapped between the blocks of the array 
        # we move the pointer which has the minimum value and calculate the amount of water trapped between the blocks of the array 
        if not arr: # if the array is empty then return 0 
            return 0    

        l, r = 0, n - 1 # left pointer is at the start of the array and the right pointer is at the end of the array  
        leftmax, rightmax = arr[l], arr[r] # leftmax is the first element of the array and rightmax is the last element of the array
        res = 0 # variable to store the amount of water trapped between the blocks of the array initialized with 0

        while l < r: # while loop to calculate the amount of water trapped between the blocks of the array
            if leftmax < rightmax: # if the leftmax is less than the rightmax then move the left pointer 
                l += 1  # increment the left pointer if the leftmax is less than the rightmax
                leftmax = max(leftmax, arr[l]) # the leftmax is the maximum of the leftmax and the current element of the array
                res += leftmax - arr[l] # the amount of water trapped between the blocks of the array is the leftmax minus the current element of the array
            else: # if the leftmax is greater than the rightmax then move the right pointer
                r -= 1 # decrement the right pointer if the leftmax is greater than the rightmax
                rightmax = max(rightmax, arr[r]) # the rightmax is the maximum of the rightmax and the current element of the array
                res += rightmax - arr[r] # the amount of water trapped between the blocks of the array is the rightmax minus the current element of the array
         
        return res # returning the amount of water trapped between the blocks of the array

n=int(input()) # taking the input value of n
arr=list(map(int,input().split()))  # taking the input values of the array seperated by space
ob = Solution() # creating an object of the class Solution
print(ob.trappingWater(arr, n)) # calling the function trappingWater with the input values and printing the output
# Input:
# 4
# 7 4 0 9
# Output:
# 10
