#Find the Runner-Up Score!
#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. You are given scores. 
#Store them in a list and find the score of the runner-up.

#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=false



if __name__ == '__main__': #if the name of the module is main
    n = int(input('enter number')) #take input from the user
    arr = map(int, input().split()) #split the input and convert it to an integer and store it in a list called arr
    scores = list(arr) #convert the map object to a list called scores
    unique_scores = list(set(scores))#convert the list to a set to remove duplicates and then convert it back to a list
    unique_scores.sort(reverse=True) #sort the list in descending order

    runner_up_score = unique_scores[1] #get the second element in the list
    print("Runner-up score:", runner_up_score)#print the runner-up score
    