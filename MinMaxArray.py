import numpy as np

def task(arr):
        np_array = np.array(arr)
        min_array = np.min(np_array, axis=1)
        return np.max(min_array)

if __name__ == '__main__':
        arr = []
        n, m = list(map(int, input().split()))
        arr.append([n, m])
        for i in range(n):
                arr.append(list(map(int, input().split())))
        result = task(arr)
        print(result)