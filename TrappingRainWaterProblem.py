def trap():
    n = int(input())
    arr = list(map(int, input().split()))
    left = [0] * n
    right = [0] * n
    left[0] = arr[0]
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
