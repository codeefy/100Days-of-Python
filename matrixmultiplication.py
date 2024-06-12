# intialise C to Zero
# i need to consider two matrices A and B 
#I need to find the product of the two matrices
#i nedd to pick ith row of A and jth column of B
#i need to multiply the elements of the two matrices
#i need to add the products of the two matrices
#i need to store the result in the ith row and jth column of the resultant matrix
#c=[[0,0,0],[0,0,0],[0,0,0]]
#print(c)
#c=[[],[],[]] #this is a list of lists
#c[0].append(0) adding 0 to the first list of c 
#output= [[[0,0,0],[],[]]] it gives 0 to the first list of c 
#now i need to add 0 to the second and third list of c using for loop 
def initialize_mat(dim):
    c=[] #initialise an empty list
    for i in range(dim): 
        c.append([]) #add an empty list to c
    for i in range(dim): #for i in the range of the dimension 
        for j in range(dim): #for j in the range of the dimension 
            c[i].append(0) #add 0 to the ith list of c
    return c  #return the resultant matrix
def dor_product(u,v):
    dim=len(u) #get the dimension of the matrix u 
    ans=0 #initialise the answer to 0   
    for i in range(dim): #for i in the range of the dimension 
        ans=ans+(u[i]*v[i]) #multiply the ith element of u with the ith element of v and add it to the answer
    return ans # return the answer 
#x=[1,2,3] #first matrix
#y=[4,5,6] #second matrix
#print(matrix_multiplication(x,y)) #print the product of the two matrices
def row(M,i): #function to get the ith row of the matrix M
    dim=len(M) #get the dimension of the matrix M
    l=[] #initialise an empty list
    for k in range(dim): #for k in the range of the dimension 
        l.append(M[i][k]) #add the kth element of the ith row of M to l 
    return l  #return the ith row of M 
#M=[[1,2,3],[4,5,6],[7,8,9]] #matrix M
##print(row(M,0)) #print the second row of M
#output=[1,2,3]
def column(M,j):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j]) #add the kth element of the jth column of M to l
    return l #return the jth column of M 
#M=[[1,2,3],[4,5,6],[7,8,9]] #matrix M
#print(column(M,0)) #print the first column of M
#output=[1,4,7]

