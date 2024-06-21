import numpy as np

def task(arr):
        np_array = np.array(arr) # it is a 2D array with n rows and m columns   
        min_array = np.min(np_array, axis=1) #min of each row in the 2D array 
        return np.max(min_array) #max of the min of each row in the 2D array 

if __name__ == '__main__':
        arr = []
        n, m = list(map(int, input().split()))
        arr.append([n, m])
        for i in range(n):
                arr.append(list(map(int, input().split())))
        result = task(arr)
        print(result)