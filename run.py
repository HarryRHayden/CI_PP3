import time
import random

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
            "Would you like to guess a boy's name (B) or girl's name (G)?")
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
    word_completed = False
    guess_count = 6
    tries = 5
    user_guesses = []
    word_completion = "_" * len(word_to_guess)
    # Check if the user has made a previous guess
    if len(user_guesses) == 0:
        print('Good luck with your game!')
    global GUESS_COUNT
    while not word_completed and guess_count > 0:
        print(word_completion)
        user_character = input('Enter your letter: \n').upper()
        while(not user_character.isalpha()) or len(user_character) != 1:
            user_character = input(
                'That is not a valid input please enter a letter: '
                ).upper()
        if user_character in user_guesses:
            print(
                f'You have already tried {user_character}. Attempt another'
                )
        elif user_character in word_to_guess:
            print(
                f'Congratulations!! {user_character} is in the name!'
                )
            user_guesses.append(user_character)
            word_listed = list(word_completion)
            indices = [i for i, letter in enumerate(word_to_guess)
                       if letter == user_character]
            for index in indices:
                word_listed[index] = user_character
            word_completion = "".join(word_listed)
            if "_" not in word_completion:
                user_wins = 1
                return win_or_lose(user_wins)
        else:
            print(
                f'Unlucky! {user_character} is not in the name. '
                f'You now have {tries} tries left'
                )
            user_guesses.append(user_character)
            guess_count -= 1
            tries -= 1
    if tries == 0:
        user_wins = 0
        return win_or_lose(user_wins)


def win_or_lose(user_wins):
    """
    Function to check whether the user has won the game or needs to guess again
    """
    if user_wins == 1:
        print('Congratulations you have guessed the word!\n')
    else:
        print('Unlucky! You did not guess the word. Better luck next time!\n')


def main():
    boys_name, girls_name, choose_gender = choose_list(gender_guess)
    word_to_guess = which_word(boys_name, girls_name, choose_gender)
    user_guess(word_to_guess)
    while input('Do you wish to play again? Y/N \n').upper() == 'Y':
        boys_name, girls_name, choose_gender = choose_list(gender_guess)
        word_to_guess = which_word(boys_name, girls_name, choose_gender)
        user_guess(word_to_guess)


if __name__ == '__main__':
    main()