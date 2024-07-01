#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(n, Path): #function to count the valleys   
    # Write your code here
    level = 0 #initialize the level to 0   
    valleys = 0 #initialize the valleys to 0  
    for step in Path: # for each step in the Path 
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys

n = int(input())
Path = input()

print(countingValleys(n, s))


