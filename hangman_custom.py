import string


def hangman_custom():
    print("Give your secret word: ")
    user_word = input().upper()
    if user_word.isalpha() is False:
        print('Your word must consist of letters!')
        hangman_custom()
    else:
        print(50 * "-\n")
        guessed_word = len(user_word) * "_"
        number_of_tries = 10
        letters_already_used = []
        print(f"You can try to guess one letter, You have {number_of_tries} tries left: ")
        while guessed_word != user_word and number_of_tries > 0:
            user_letter = input().upper()
            if user_letter.lower() == "exit":
                break
            elif user_letter.isalpha() is False or len(user_letter) != 1:
                print("Your guess must only be a single letter!")
            elif user_letter in letters_already_used:
                print(
                    f"You have already used this letter! \n Used letters are - {sorted(letters_already_used)}"
                )
            elif user_letter in user_word:
                letters_already_used += user_letter
                print("You guessed this one correctly!")
                indexes = [i for i, letter in enumerate(user_word) if letter == user_letter]
                guessed_word = list(guessed_word)
                for index in indexes:
                    guessed_word[index] = user_letter
                guessed_word = "".join(guessed_word)
                print(guessed_word)
                print(f"Letters already used are: {sorted(letters_already_used)}")
            elif user_letter not in user_word:
                letters_already_used += user_letter
                number_of_tries -= 1
                print(f"Wrong guess, You have {number_of_tries} tries left.")
                print(f"Letters already used are: {sorted(letters_already_used)}")
                print(guessed_word)
            elif guessed_word != user_word and number_of_tries <= 0:
                print("Game over.")
                print(f"The word you were trying to guess is: {user_word}")
        if guessed_word == user_word:
            print(
                f"Good job! You guessed the word {user_word.upper()} correctly! Guesses left: {number_of_tries}"
            )
        elif number_of_tries <= 0:
            print("Game over, You ran out of tries.")
