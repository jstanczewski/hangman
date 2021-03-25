from words import words
import random


def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman_random():
    word = get_word(words).upper()
    number_of_tries = 10
    guessed_word = len(word) * '_'
    letters_already_used = []
    print(f"You can try to guess one letter, You have {number_of_tries} tries left: ")
    while guessed_word != word and number_of_tries > 0:
        user_letter = input().upper()
        if user_letter.lower() == 'exit':
            break
        elif user_letter.isalpha() is False or len(user_letter) != 1:
            print("Your guess must only be a single letter!")
        elif user_letter in letters_already_used:
            print(f"You have already used this letter! \n Used letters are - {sorted(letters_already_used)}")
        elif user_letter in word:
            print('Correct guess!')
            letters_already_used += user_letter
            indexes = [i for i, letter in enumerate(word) if letter == user_letter]
            guessed_word = list(guessed_word)
            for index in indexes:
                guessed_word[index] = user_letter
            guessed_word = ''.join(guessed_word)
            print(guessed_word)
            print(f"Letters already used are: {sorted(letters_already_used)}")
        elif user_letter not in word:
            letters_already_used += user_letter
            number_of_tries -= 1
            print(f'Wrong guess, You have {number_of_tries} tries left.')
            print(f"Letters already used are: {sorted(letters_already_used)}")
            print(guessed_word)
        elif guessed_word != word and number_of_tries <= 0:
            print("Game over.")
            print(f"The word you were trying to guess is: {word}")
    if guessed_word == word:
        print(
            f"Good job! You guessed the word {word.upper()} correctly! You had {number_of_tries} left."
        )
    elif number_of_tries <= 0:
        print("Game over, You ran out of tries.")
        print(f'The word you were trying to guess is: {word}')
