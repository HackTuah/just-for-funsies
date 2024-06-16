import random

# Import necessary modules
# Random module will be used for computer's choice

# Define a function to get the computer's move
def get_computer_move():
    """
    Randomly choose one of the options: rock, paper, or scissors
    """
    return random.choice(['rock', 'paper', 'scissors'])

# Define a function to determine the winner
def determine_winner(player_move, computer_move):
    """
    Determine the winner based on the rules:
    Rock beats scissors, Scissors beat paper, Paper beats rock.
    Return 'win' if the player wins, 'lose' if the player loses, and 'tie' if it's a tie.
    """
    if player_move == computer_move:
        return 'tie'
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'scissors' and computer_move == 'paper') or \
         (player_move == 'paper' and computer_move == 'rock'):
        return 'win'
    else:
        return 'lose'

# Define a function to get the player's move
def get_player_move():
    """
    Prompt the player to enter a move: rock, paper, or scissors.
    Convert the input to lowercase and check if it's a valid move.
    If the move is invalid, inform the player and prompt again.
    """
    while True:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        if move in ['rock', 'paper', 'scissors']:
            return move
        else:
            print("Invalid move. Please enter rock, paper, or scissors.")

# Define the main function to play the game
def play_game():
    """
    Main game loop:
    - Get the player's move
    - Get the computer's move
    - Determine the winner
    - Display the result
    - Ask if the player wants to play again
    - Keep track of the player's score
    - Display the score at the end of the game
    """
    player_score = 0
    computer_score = 0
    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        print(f"Computer chose: {computer_move}")
        result = determine_winner(player_move, computer_move)
        if result == 'win':
            print("You win!")
            player_score += 1
        elif result == 'lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Final Score: You {player_score} - {computer_score} Computer")

# Start the game
if __name__ == "__main__":
    play_game()
