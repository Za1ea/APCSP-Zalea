import random

words = ["smart", "broil", "amber", "plate", "quilt", "wreck", "clout", "vices"]

word = random.choice(words)

# colors
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def gen_hint(guess):
    color = default
    hint = ''

    for i, letter in enumerate(guess):
        if letter in word:
            if letter == word[i]:
                color = green
            else:
                color = yellow
        else:
            color = default
        hint = hint + color + letter + default
    return hint


def game_loop():
    for i in range(6):
        guess = input("What is your guess: ")
        print(gen_hint(guess))

        if (guess == word):
            print("You guessed it! Congratulations!")
            break

game_loop()