#There are three robots named Ray, Ben and Kevin. Initially Ray has a string S of length N.
#while the other two robots have empty strings. We can make either of the following moves:
#Move |: Remove the first character from Ray’s string and append it to Ben’s string.
#Move 2:Remove the last character from Ben’s string and append it to Kvin’s string.
#You must perform either of the two moves mentioned above in such a way that the strings left
#with Ray and Ben are empty and the string left with Kevin is lexicographically the smallest.
#Your task is to return this lexicographically smallest string that Kevin has after completing this activity.
#Note: For any two given strings, a string is said to be lexicographically smaller than the other
#if it comes before the other string in the dictionary

ray = input() # taking the input value of the string S
n = len(ray) # length of the string S
ben = "" # string of Ben is empty
kevin = "" # string of Kevin is empty
i = 0 # variable to store the index of the string S
j = 0 # variable to store the index of the string of Ben
k = 0 # variable to store the index of the string of Kevin
while i < n: # while loop to perform the moves
    if ben == "" or ben[0] < ray[i]: # if the string of Ben is empty or the first character of the string of Ben is less than the current character of the string S
        ben = ben + ray[i] # append the current character of the string S to the string of Ben
        i += 1 # increment the index of the string S
    else: # if the first character of the string of Ben is greater than the current character of the string S
        kevin = ben[0] + kevin # append the first character of the string of Ben to the string of Kevin
        ben = ben[1:] # remove the first character of the string of Ben
while j < len(ben): # while loop to perform the moves
    kevin = ben[j] + kevin # append the current character of the string of Ben to the string of Kevin
    j += 1 # increment the index of the string of Ben
print(kevin) # printing the lexicographically smallest string that Kevin has after completing this activity

#Input:
#abcde
#Output:
#abcde
#Input:
#cbade
#Output:
#abcde