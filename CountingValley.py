#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(n, s): #function to count the valleys   
    # Write your code here
    level = 0
    valleys = 0
    for step in s:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys

n = int(input())
s = input()

print(countingValleys(n, s))


