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
