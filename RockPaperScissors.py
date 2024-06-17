# write code for rock paper and scissior game using python 
# rock beats scissor
# scissor beats paper
# paper beats rock
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
#The minigame should inform the player whether the player won, lost, or tied with the opponent.
#Choose to continue playing.
#At the prompt, type screen.
#the minigame should inform the player if the option entered by the player is invalid.
#Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.
#Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.


import random  #import the random module to generate random numbers 
def rock_paper_scissors(): 
    player_score=0 #initialise the player score to 0
    computer_score=0    #initialise the computer score to 0
    while True: #while the condition is true  
        player=input("Enter rock, paper or scissors: ") #get the input from the player
        computer=random.choice(["rock","paper","scissors"]) #get the input from the computer
        print("Computer chose: ",computer) # print the choice of the computer  
        if player.lower() not in ["rock","paper","scissors"]:
            print("Invalid option")
            continue
        if player.lower()==computer:
            print("Tie")
        elif player.lower()=="rock":
            if computer=="scissors":
                print("You win")
                player_score+=1
            else:
                print("You lose")
                computer_score+=1
        elif player.lower()=="scissors":
            if computer=="paper":
                print("You win")
                player_score+=1
            else:
                print("You lose")
                computer_score+=1
        elif player.lower()=="paper":
            if computer=="rock":
                print("You win")
                player_score+=1
            else:
                print("You lose")
                computer_score+=1
        print("Player score: ",player_score)
        print("Computer score: ",computer_score)
        play_again=input("Do you want to play again? ")
        if play_again.lower()!="yes":
            break
rock_paper_scissors()

#output
#Enter rock, paper or scissors: rock
#Computer chose:  rock
#Tie