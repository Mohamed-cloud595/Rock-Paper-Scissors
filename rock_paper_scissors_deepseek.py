import random
import sys
from enum import Enum

class Choice(Enum):
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'

def get_user_choice():
    """Get and validate user input."""
    while True:
        user_input = input("\nChoose: 'r' (Rock), 'p' (Paper), 's' (Scissors), or 'q' (Quit)\n> ").lower()
        if user_input in [choice.value for choice in Choice] + ['q']:
            return user_input
        print("❌ Invalid input. Try again!")

def determine_winner(user, pc):
    """Determine the winner based on choices."""
    if user == pc:
        return "tie"
    
    winning_combinations = {
        Choice.ROCK.value: Choice.SCISSORS.value,
        Choice.PAPER.value: Choice.ROCK.value,
        Choice.SCISSORS.value: Choice.PAPER.value
    }
    
    return "user" if winning_combinations[user] == pc else "pc"

def print_choice(choice):
    """Convert choice letter to full word for display."""
    choice_map = {
        'r': '✊ Rock',
        'p': '✋ Paper',
        's': '✌ Scissors'
    }
    return choice_map.get(choice, 'Unknown')

def play_game():
    """Main game loop."""
    print("\n🔥 Welcome to Rock-Paper-Scissors! 🔥")
    print("----------------------------------")
    
    user_score = 0
    pc_score = 0
    ties = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            print("\n📊 Final Score:")
            print(f"🏆 You: {user_score} | 🤖 Computer: {pc_score} | 🤝 Ties: {ties}")
            print("Thanks for playing! Goodbye. 👋")
            sys.exit()
            
        pc_choice = random.choice([choice.value for choice in Choice])
        
        print(f"\nYou played: {print_choice(user_choice)}")
        print(f"Computer played: {print_choice(pc_choice)}")
        
        result = determine_winner(user_choice, pc_choice)
        
        if result == "tie":
            print("🤝 It's a tie!")
            ties += 1
        elif result == "user":
            print("🎉 You won!")
            user_score += 1
        else:
            print("😢 You lose!")
            pc_score += 1
            
        print(f"\n📊 Score: You: {user_score} | Computer: {pc_score} | Ties: {ties}")
        print("----------------------------------")

if __name__ == "__main__":
    play_game()