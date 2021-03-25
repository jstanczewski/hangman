from hangman_custom import hangman_custom
from hangman_random import hangman_random


def game():
    print('What mode do You chose? Type \'custom\' if You want to come up with Your own word. Type \'random\' if You want a random word to guess.')
    user_input = input()
    if user_input.lower() == 'custom':
        hangman_custom()
    elif user_input.lower() == 'random':
        hangman_random()
    else:
        print('Invalid input, must be either \'custom\' or \'random\' (capitalization does not matter).')


print('Do You want to play hangman? Type \'yes\' or \'no\'.')
while True:
    if input().lower() == 'yes':
        game()
        print('Type \'yes\' if You want to play again.')
    else:
        print('Bye. :(')
        break
