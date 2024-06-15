import numpy 
#The first N line contains the integer .
N = int(input())

#The next  lines contains the  space separated elements of array .

arr = numpy.array([input().split() for _ in range(N)],float)

#print the determinant of arr
#2
#1.1 1.1
#1.1 1.1
print(round(numpy.linalg.det(arr), 2))

#Output
#0.0