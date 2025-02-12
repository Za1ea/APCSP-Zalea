import random
import string
import requests

password_length = int(input('How many characters do you want your password to be?'))

# generate single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

def generate_strong_password():
    password = ''
    for i in range(password_length):
        password = password + random_character()
    print(password)

def fetch_word(num):
    url = f"https://random-word-api.herokuapp.com/word?length={num}"

    response = requests.get(url)
    word = response.json()[0]
    # print(word)
    return word

def replace_letters(word):
    word = word[0].upper() + word[1:]
    replace_letters_dict = {
        "a": "@",
        "e": "3",
        "h": "#",
        "i": "!",
        "j": ";",
        "l": "1",
        "n": "^",
        "o": "0",
        "u": "v"
    }
    for (letter,replacement) in replace_letters_dict.items():
        word = word.replace(letter, replacement)
    # print(word)
    return word

def generate_weaker_password():
    word1 = fetch_word(8)
    word2 = fetch_word(6)
    word1 = replace_letters(word1)
    word2 = replace_letters(word2)
    password = word1 + word2
    print(password)

generate_strong_password()
generate_weaker_password()