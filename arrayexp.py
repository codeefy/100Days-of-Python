import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = list(map(float, arr))
    arr.reverse()
    
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)