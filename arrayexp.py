# reverse the array and convert it into float array using numpy 

import numpy

def arrays(arr):  #arr is a list of integers separated by space  
    # complete this function
    # use numpy.array
    arr = list(map(float, arr)) #convert the list of integers to a list of floats  
    arr.reverse() #reverse the list of floats 
    
    return numpy.array(arr, float) #return the reversed list of floats as a numpy array of floats 

arr = input().strip().split(' ') #input is a list of integers separated by space    
result = arrays(arr)
print(result)