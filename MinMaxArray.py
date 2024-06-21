import numpy as np

def task(arr):
        np_array = np.array(arr) # it is a 2D array with n rows and m columns   
        min_array = np.min(np_array, axis=1) #min of each row in the 2D array 
        return np.max(min_array) #max of the min of each row in the 2D array 

if __name__ == '__main__': # main function to take input from the user and print the output 
        arr = [] # list to store the input values  
        n, m = list(map(int, input().split())) # taking the input values of n and m seperated by space 
        arr.append([n, m]) # appending the values of n and m to the list 
        for i in range(n): # for loop to take the input values of the 2D array
                arr.append(list(map(int, input().split()))) # appending the input values of the 2D array to the list
        result = task(arr) # calling the function task with the input values
    
        print(result) # printing the output