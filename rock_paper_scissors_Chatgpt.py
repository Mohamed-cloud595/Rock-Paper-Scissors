import random

def get_user_choice():
    choices = {'r': 'Rock', 
               'p': 'Paper',
               's': 'Scissors'}
    while True:
        user_input = input("Enter your choice: (r)ock, (p)aper, or (s)cissors: ").lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("Invalid choice. Please select 'r', 'p', or 's'.")

def get_pc_choice():
    choices = {'r': 'Rock',
               'p': 'Paper',
               's': 'Scissors'}
    pc_input = random.choice(list(choices.keys()))
    return pc_input, choices[pc_input]

def determine_winner(user, pc):
    win_conditions = {
        'r': 's',  # Rock beats Scissors
        'p': 'r',  # Paper beats Rock
        's': 'p'   # Scissors beats Paper
    }
    if user == pc:
        return "It's a tie!"
    elif win_conditions[user] == pc:
        return "You won!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_key, user_choice = get_user_choice()
        pc_key, pc_choice = get_pc_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Pc chose: {pc_choice}")
        result = determine_winner(user_key, pc_key)
        print(result)

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# Run the game
play_game()
