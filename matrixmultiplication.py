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
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        c[i].append(0)
    return c