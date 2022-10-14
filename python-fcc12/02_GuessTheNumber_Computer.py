

"""
Description: game for user to guess computer's secret number
Lesson: use functions,
1 - Generate computer number with "random" package
"""


# Import this package to use relevant functions, namely "random.randint" 
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number beteween 1 and {x}: '))
        # print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


guess(10)