name = int(input())  # get the input from the user  
playlist = input().split(" ")  # get the input from the user and split it by space  

def count_favourite_singers(playlist):  #function to count the favourite singers in the playlist 
    singer_count = {}  #initialise an empty dictionary  
    for singer in playlist: #for each singer in the playlist 
        if singer in singer_count:             
            singer_count[singer] += 1         
        else:             
            singer_count[singer] = 1 

    max_count = max(singer_count.values())
    favourite_singers_count = sum(1 for count in singer_count.values() if count == max_count)
    
    return favourite_singers_count 

print(count_favourite_singers(playlist))
