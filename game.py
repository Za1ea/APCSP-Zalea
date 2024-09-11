import random

def generate_cups(num_cups):
    # Fixed list of colors
    colors = ['R', 'B', 'G', 'Y', 'P', 'O']  # Red, Blue, Green, Yellow, Purple, Orange
    if num_cups > len(colors):
        raise ValueError("Number of cups cannot be more than the number of available colors.")
    return random.sample(colors, num_cups)

def get_user_guess(num_cups):
    print(f"Enter your guess for the order of {num_cups} cups. Choose from: R, B, G, Y, P, O")
    guess = []
    guess_str = input('Cup Order with no spaces:').upper()
    for color in guess_str:
        if color not in ['R', 'B', 'G', 'Y', 'P', 'O']:
            print(f"Invalid input {color}. Please enter a valid letter.")
            return get_user_guess(num_cups)  # Restart if the input is invalid
        guess.append(color)
    return guess

def evaluate_guess(correct_order, user_guess):
    correct_positions = sum([1 for i in range(len(correct_order)) if correct_order[i] == user_guess[i]])
    return correct_positions

def cup_game():
    num_cups = int(input("Enter the number of cups (between 2 and 6): "))
    if num_cups < 2 or num_cups > 6:
        print("Please enter a number between 2 and 6.")
        return cup_game()  # Restart if the number of cups is invalid

    correct_order = generate_cups(num_cups)
    print("The cups have been shuffled. Try to guess their order!")

    while True:
        user_guess = get_user_guess(num_cups)
        correct_positions = evaluate_guess(correct_order, user_guess)

        if correct_positions == num_cups:
            print(f"\nCongratulations! You guessed the correct order: {correct_order}")
            break
        else:
            print(f"You have {correct_positions} cup(s) in the correct position. Try again!")

if __name__ == "__main__":
    cup_game()
