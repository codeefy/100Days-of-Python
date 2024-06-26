# Problem: The Minion Game from HackerRank - Python Solution    
# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# For better understanding, see the image below:
# banana.png
# Your task is to determine the winner of the game and their score.
#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false
#Input Format
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: 
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)

