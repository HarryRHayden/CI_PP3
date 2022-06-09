import time, random

# Lists for potential words to guess
gender_guess = {
    'boys_names': ['Luke', 'Harry', 'Edward', 'William', 'Lewis', 'Gregory'],
    'girl_names': ['Georgina', 'Elizabeth', 'Lucy', 'Louise', 'Ellie']
}


def choose_list(gender_guess):
    """
    Loop until player has chosen a list to guess from
    """
    choose_gender = input(
        "Would you like to guess a boy's name (B) or girl's name (G)?\n"
    ).upper()
    # Give random choice for each list
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


def user_guess(word_to_guess):
    """
    For user to input their character guesses. Disallowing numerical input
    """
    guess_count = 6
    user_guesses = []
    word_completion = "_" * len(word_to_guess)
     # Check if the user has made a previous guess
    if len(user_guesses) == 0:
        print('Good luck with your game!')
    global GUESS_COUNT
    print(word_completion)
    user_character = input('Enter your letter: ').upper()
    while(not user_character.isalpha()) or len(user_character) != 1:
        user_character = input(
            'That is not a valid input please enter a letter: '
            ).upper()
    if user_character in word_to_guess:
        print(
            f'Congratulations!! {user_character} is in the name!'
            )
    elif user_character in user_guesses:
        print(
            f'You have already tried {user_character}. Attempt another letter'
            )
    else:
        guess_count -= 1

        print(
            f'Unlucky! {user_character} is not in the name'
            f'You now have {guess_count} number of tries left'
        )


def win_or_lose(user_wins):
    """
    Function to check whether the user has won the game or needs to guess again
    """


boys_name, girls_name, choose_gender = choose_list(gender_guess)
word_to_guess = which_word(boys_name, girls_name, choose_gender)
user_guess(word_to_guess)