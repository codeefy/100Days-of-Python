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

# write driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.trappingWater(arr, n))

