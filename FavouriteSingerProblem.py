# Description: A program that takes an integer n and a list of n strings as input and returns the number of favourite singers in the list. A favourite singer is a singer that appears the most number of times in the list. If there are multiple singers that appear the most number of times, then all of them are considered favourite singers.
#  
# Input: The input consists of two lines. The first line contains an integer n (1 ≤ n ≤ 100) which represents the number of singers in the list. The second line contains n strings separated by a space, which represents the list of singers. Each singer is a string of lowercase English letters with a length of at most 100.
name = int(input())  # get the input from the user  
playlist = input().split(" ")  # get the input from the user and split it by space  

def count_favourite_singers(playlist):  #function to count the favourite singers in the playlist 
    singer_count = {}  #initialise an empty dictionary  
    for singer in playlist: #for each singer in the playlist 
        if singer in singer_count:   #if the singer is in the singer count            
            singer_count[singer] += 1    #increment the count of the singer by 1      
        else:             # if the singer is not in the singer count 
            singer_count[singer] = 1  #add the singer to the singer count and set the count to 1

    max_count = max(singer_count.values()) #get the maximum count of the singers
    favourite_singers_count = sum(1 for count in singer_count.values() if count == max_count) # get the count of the favourite singers  and sum it  if the count is equal to the maximum count
    
    return favourite_singers_count  #return the count of the favourite singers

print(count_favourite_singers(playlist)) #print the count of the favourite singers in the playlist    
