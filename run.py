import time, random

# Lists for potential words to guess
gender_guess = {
    'boys_names': ['Luke', 'Harry', 'Edward', 'William', 'Lewis', 'Gregory'],
    'girl_names': ['Georgina', 'Elizabeth', 'Lucy', 'Louise', 'Ellie']
}

# Empty list for users guesses
USER_GUESSES = []
# How many guesses the user gets
GUESS_COUNT = 7


def choose_list(gender_guess):
    """
    Loop until player has chosen a list to guess from
    """
    choose_gender = input(
        "Would you like to guess a boy's name (B) or girl's name (G)?\n"
    )
    boys_name = random.choice(gender_guess['boys_names'])
    girls_name = random.choice(gender_guess['girl_names'])
    while not (
        choose_gender == 'G' or choose_gender == 'B'
    ):
        choose_gender = input(
            "Would you like to guess a boy's name (B) or girl's name (G)?"
    )
    return [boys_name.upper(), girls_name.upper(), choose_gender]


def which_word(boys_name, girls_name, choose_gender):
    """
    Determins the word to be guessed
    """
    if choose_gender == 'G':
        chosen_word = girls_name
    else:
        chosen_word = boys_name
    return chosen_word
GeneratorExit()

def user_guess(word_to_guess, USER_GUESSES):
    """
    For user to input their character guesses. Disallowing numerical input
    """
    print('Your word to guess is below:')
    display_under = '_' * len(word_to_guess)
    print(display_under)
    global GUESS_COUNT
    character_chosen = input('Choose a letter:\n').upper()
    print(character_chosen)


boys_name, girls_name, choose_gender = choose_list(gender_guess)
word_to_guess = which_word(boys_name, girls_name, choose_gender)
user_guess(word_to_guess, USER_GUESSES)
print(word_to_guess)