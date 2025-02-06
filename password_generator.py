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
    return word

generate_strong_password()
print(fetch_word(5))