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
        res = 0

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, arr[l])
                res += leftmax - arr[l]
            else:
                r -= 1
                rightmax = max(rightmax, arr[r])
                res += rightmax - arr[r]
        
        return res

n=int(input())
arr=list(map(int,input().split()))
ob = Solution()
print(ob.trappingWater(arr, n))
# Input:
# 4
# 7 4 0 9
# Output:
# 10
