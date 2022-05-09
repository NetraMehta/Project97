import random

print("Instructions: Guess a number from 0-20. You will get hints for your guesses. You will get 5 chances. Enjoy!")

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random = (random.choice(list))

guess1 = int(input('Guess a number from 0-20: '))

if guess1 < random :
    print('Guess too small')

elif guess1 > random :
    print('Guess too big')

elif guess1 == random :
    print('Congragulations! You Won!')


if guess1 != random :
    guess2 = int(input('Guess a number from 1-9: '))

    if guess2 < random :
        print('Guess too small')

    elif guess2 > random :
        print('Guess too big')

    elif guess2 == random :
        print('Congragulations! You Won!')


if guess2 != random :
    guess3 = int(input('Guess a number from 1-9: '))

    if guess3 < random :
        print('Guess too small')

    elif guess3 > random :
        print('Guess too big')

    elif guess3 == random :
        print('Congragulations! You Won!')


if guess3 != random :
    guess4 = int(input('Guess a number from 1-9: '))

    if guess4 < random :
        print('Guess too small')

    elif guess4 > random :
        print('Guess too big')

    elif guess4 == random :
        print('Congragulations! You Won!')


if guess4 != random :
    guess5 = int(input('Guess a number from 1-9: '))

    if guess5 != random :
        print('You lost. Better luck next time. The number was... ', random)

    elif guess5 == random :
        print('Congragulations! You Won!')