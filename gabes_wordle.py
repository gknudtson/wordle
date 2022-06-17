import random
from termcolor import colored

#VARIABLES
keep_playing = 'yes'
word_bank = []

#FUNCTIONS
def playing():
    global keep_playing
    keep_playing = input('Would you like to play again? (yes , no) ').lower()

def random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

def get_word_bank():
    with open("words.txt") as f:
        word_bank = f.read().splitlines()
        return 

def get_word_bank():
    f = open("words.txt", "r")
    content = f.read().splitlines()
    global word_bank
    word_bank = content

def letter_colors(user_guess, secret_word):
    counter = 0
    for letter in user_guess:
        user_guess_count = user_guess.count(letter, 0, counter)
        secret_word_count = secret_word.count(letter)

        if letter == secret_word[counter]:
            print(colored(user_guess[counter], 'green'), end = "")

        elif letter in secret_word and user_guess_count < secret_word_count:
            print(colored(user_guess[counter], 'yellow'), end = "")
            
        else:
            print(user_guess[counter], end = '')
        
        counter += 1
    print('\n')

#GAME LOOP
while keep_playing == 'yes':
    player = 'lost'
    secret_word = random_word()
    get_word_bank()

    for guess_count in range(1, 7):
    
        user_guess = input('Please enter a 5 letter word. ').lower()
        print(f'Guess number: {guess_count}')

        while user_guess not in word_bank:
            user_guess = input('Invalid input, please enter a 5 letter word. ').lower()

        if user_guess == secret_word:
            print(f'Congratulations, the word was {secret_word} it took you {guess_count} guesses.')
            playing()
            player = 'won'
            break

        else:
            letter_colors(user_guess, secret_word)

    if player == 'lost':
        print(f"You lost the word was: {secret_word}")
        playing()