import os
from random import choice
from string import ascii_lowercase

DICT_SUBFOLDER = 'data'
DICT_FILENAME = 'sowpods.txt'


def get_rand_word(dict_filename):
    with open(dict_filename, 'r') as f:
        return choice([x.strip() for x in f]).lower()


def print_game(guessed_word, wrong_letters, guessed_word_letters):
    print('-----------------------------------------------------------')
    print('Wrong guess:', ', '.join(wrong_letters))

    output_line = ''
    for i in guessed_word_letters:
        output_line += '  ' if i is None else i + ' '
    print(output_line)

    print('_ ' * len(guessed_word))


def get_letter(attempts, guess):
    hint = 'english lowercase'
    user_input = input(f'> Guess a {hint} letter ('
                       f'{attempts} attempts left): ').lower()

    if len(user_input) != 1 or user_input not in ascii_lowercase:
        print(f'Please input a {hint} letter!')
        return None
    elif user_input in guess:
        print(f"> You have guessed '{user_input}' before")
        return None
    else:
        return user_input


def play(hidden_word, attempts):
    guess, wrong_guess = [], []
    guessed_letters = [None] * len(hidden_word)

    while attempts > 0:
        print_game(hidden_word, wrong_guess, guessed_letters)

        if None not in guessed_letters:
            print('> You win!')
            return

        user_letter = get_letter(attempts, guess)

        if user_letter is None:
            continue
        for letter_index, letter in enumerate(hidden_word):
            if user_letter == letter:
                guessed_letters[letter_index] = user_letter
        guess.append(user_letter)

        if user_letter in guessed_letters:
            continue
        wrong_guess.append(user_letter)
        attempts -= 1

    print_game(wrong_guess, hidden_word, guessed_letters)
    print('> You lose...')
    print(f'> Answer: {hidden_word.capitalize()}')


if __name__ == "__main__":
    dict_filename = os.path.join(DICT_SUBFOLDER, DICT_FILENAME)
    try:
        play(get_rand_word(dict_filename), 6)
    except FileNotFoundError:
        print(f'Error! Dictionary {DICT_FILENAME} not found!'
              f' Create {dict_filename} in working folder before playing')
    except IndexError:
        print(f'Error! Dictionary {DICT_FILENAME} is empty!'
              'Fill it with words before playing')
