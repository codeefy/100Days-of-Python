#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(Steps, Path): #function to count the valleys   
    # Write your code here
    level = 0 #initialize the level to 0   
    valleys = 0 #initialize the valleys to 0  
    for step in Path: # for each step in the Path 
        if step == 'U': #if the step is U, increment the level by 1 
            level += 1 # increment the level by 1 
            if level == 0: #if the level is 0, increment the valleys by 1 
                valleys += 1 #increment the valleys by 1
        else: #if the step is D, decrement the level by 1 
            level -= 1 #decrement the level by 1
    return valleys #return the number of valleys 

Steps = int(input()) #read the number of steps  
Path = input() #read the path 

print(countingValleys(Steps, Path)) # print the number of valleys 

#input
#8
#UDDDUDUU
#output
#1



