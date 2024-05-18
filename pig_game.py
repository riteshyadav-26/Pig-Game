# importing random module
import random

# defining a function to generater random whole number's between one and six
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Asking user's input for how many players want to play
while True:
    players = input('Enter the number of players want to play (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:       # Number of player's must be between 2 and four
            break
        else:
            print('Invalid input!. Must be between 2 & 4. Try again...')        
    else:
        print('Invalid input!. Must be a digit. Try again...')
        
# maximum score target
max_score = 10
# creating a list to store player's score
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    # Looping through every player's turn
    for player_idx in range(players):
        # To track score of player
        current_score = 0

        while True:
            print(f'\nPlayer {player_idx+1}\'s turn.\n')
            should_roll = input('Would you like to roll (y/n): ').lower()

            if should_roll == 'y':
                value = roll()

                if value == 1:
                    print(f'You rolled a {value}!. Turn done!')
                    current_score = 0
                    break
                else:
                    print(f'You rolled a {value}.')
                    current_score += value

            elif should_roll == 'n':
                break
            else:
                print('Invalid input!. Must be [y/n]. Try again...')
                continue  
              
        player_scores[player_idx] += current_score
        print(f'Your score is {player_scores[player_idx]}')

player = player_scores.index(max(player_scores))
print(f'Player {player+1} wins!')
