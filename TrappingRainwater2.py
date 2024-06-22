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

class Solution: 
    def trappingWater(self, arr, n):
        # Two-pointer approach
        if not arr:
            return 0

        l, r = 0, n - 1
        leftmax, rightmax = arr[l], arr[r]
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
