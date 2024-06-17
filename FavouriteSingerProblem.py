name = int(input()) 
playlist = input().split(" ") 

def count_favourite_singers(playlist): 
    singer_count = {} 
    for singer in playlist:
        if singer in singer_count:             
            singer_count[singer] += 1         
        else:             
            singer_count[singer] = 1 

    max_count = max(singer_count.values())
    favourite_singers_count = sum(1 for count in singer_count.values() if count == max_count)
    
    return favourite_singers_count 

print(count_favourite_singers(playlist))
