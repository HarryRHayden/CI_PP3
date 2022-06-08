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
    ).upper()
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


def user_guess(word_to_guess, USER_GUESSES):
    """
    For user to input their character guesses. Disallowing numerical input
    """
    print('Your word to guess is below:')
    display_under = '_' * len(word_to_guess)
    print(display_under)
    global GUESS_COUNT
    print(word_to_guess)
    user_character = input('Enter your letter: ').upper()
    while(not user_character.isalpha()) or len(user_character) != 1:
        user_character = input(
            'That is not a valid input please enter a letter: '
            ).upper()
    if user_character in word_to_guess:
        print(
            f'Congratulations!! {user_character} is in the name!'
            )
    elif user_character in USER_GUESSES:
        print(
            f'You have already tried {user_character}. Attempt another letter'
            )
    else:
        GUESS_COUNT -= 1
        print(
            f'Unlucky! {user_character} is not in the name'
            f'You now have {GUESS_COUNT} number of tries left'
        )
    return win_or_lose(USER_GUESSES, user_character, word_to_guess)


def win_or_lose(USER_GUESSES, user_character, word_to_guess):


boys_name, girls_name, choose_gender = choose_list(gender_guess)
word_to_guess = which_word(boys_name, girls_name, choose_gender)
user_guess(word_to_guess, USER_GUESSES)
print(word_to_guess)