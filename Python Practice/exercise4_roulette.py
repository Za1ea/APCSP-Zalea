import random
import time

# function to generate wheel
def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    money = 100
    spaces = generate_wheel()
    play_again = True
    
    print(f"You have ${money}.")
    while True:
        bet = int(input("How much do you want to bet?\n"))
        color = input("What color do you want to bet on?\n")

        print("The wheel is spinning. Good luck...")
        time.sleep(2)
        landed = spin_wheel(spaces)
        print(f"It landed on {landed}.")

        if landed == color:
            money += bet
            print(f"Congrats! You now have ${money}")
        else:
            money -= bet
            print(f"Sorry! You now have ${money}")
        play_again = input("Do you want to play again? If not type 'no', otherwise type anything")
        if play_again.lower() == "no":
            break

    

play_game()