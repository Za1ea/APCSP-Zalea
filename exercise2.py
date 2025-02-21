import random

random_num = random.randint(0, 100)

num_guesses = 0

while True:
    guess = int(input("Guess a number \n"))
    num_guesses += 1

    if guess < random_num:
        print("Guess higher")
    elif guess > random_num:
        print("Guess lower")
    else:
        print(f"You got it in {num_guesses} guesses!")
        break