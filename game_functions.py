import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    difference=next_val-current_val
    if difference<0:
        highOrLow="l"
    elif difference>0:
        highOrLow="h"
    if highOrLow==user_input:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found=False
    wordLetters=list(word)
    for x in range(0, len(wordLetters)):
        if wordLetters[x]==letter:
            board[x]=letter
            found=True
    if found==True:
        print(f"Well Done! '{letter}' is in the word")
        return True
    else:
        print(f"Sorry, '{letter}' is not in the word")
        return False
    