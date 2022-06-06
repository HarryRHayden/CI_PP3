import time, random

# Lists for potential words to guess
gender_guess = {
    'boys_names' : ['Luke', 'Harry', 'Edward', 'William', 'Lewis', 'Gregory'],
    'girl_names' : ['Georgina', 'Elizabeth', 'Lucy', 'Louise', 'Ellie']
}

# Empty list for users guesses
user_guesses = []
# How many guesses the user gets
GUESS_COUNT = 7


def choose_list(gender):
    """
    Loop until player has chosen a list to guess from
    """
    choose_gender = input(
        "Would you like to guess a boy's or girl's name?"
    )
    print(choose_gender)


choose_list(gender_guess)