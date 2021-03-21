# Author: Sloane Luckiewicz
# Rock, Paper, Scissors and Functions

import random 

def play_game():
    win = 0
    lose = 0
    tie = 0

    print("Welcome to Rock, Paper, Scissors!")
    play_multiple = input("Would you like to (P)lay or (Q)uit? ").lower().strip()

    while play_multiple == "p":
            
        # choices
        comp_choice = get_comp_choice()
        player_choice = get_player_choice()
        print(f"Computer chose {comp_choice}")
        print(f"You chose {player_choice}")

        # results
        winning_results(comp_choice, player_choice)

        # play again
        play_multiple = input("Would you like to (P)lay or (Q)uit? ").lower().strip()
    
    # quit
    else: 
        print("Goodbye")
     
    # tally
    print(f"""Your total wins are {win}. Your total losses are {lose}. Your total ties are {tie}. """)

# computer choice
def get_comp_choice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "rock"
    elif comp_choice == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"
            
    return comp_choice

# player choice
def get_player_choice():
    player_choice = int(input("Choose rock(1), paper(2), or scissors(3): "))

    if player_choice == 1:
        player_choice = "rock"
    elif player_choice == 2:
        player_choice = "paper"
    elif player_choice == 3:
        player_choice = "scissors"
    else:
        print("Invalid input.")
        player_choice = int(input("Choose rock(1), paper(2), or scissors(3): "))
        
    return player_choice

# results
def winning_results(comp_choice, player_choice):
    win = 0
    lose = 0
    tie = 0
    if comp_choice == player_choice:
        winning_results = "tie"
        tie += 1
        print("You tied!")
    elif comp_choice == "scissors" and player_choice == "rock":
        winning_results = "win"
        win += 1
        print("Rock beats scissors. You win!")
    elif comp_choice == "paper" and player_choice == "scissors":
        winning_results = "win"
        win +=1
        print("Scissors cuts paper. You win!")
    elif comp_choice == "rock" and player_choice == "paper":
        winning_results = "win"
        win +=1
        print("Paper beats rock. You win!")
    else:
        winning_results = "lose"
        lose +=1
        print("You lose!")
        
    return winning_results
        
    print(f"""Your total wins are {win}. Your total losses are {lose}. Your total ties are {tie}. """)
    print("Goodbye!")


play_game()
