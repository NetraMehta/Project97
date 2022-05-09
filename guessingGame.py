import random

print("Instructions: Guess a number from 1-9. If the difference between the number is 2 or more, you will get a hint saying that the number is too big or too small. If you're number is close to the actual number, you will get a hint saying that the guess was close. You will get 5 chances. Enjoy!")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random = (random.choice(list))

guess1 = int(input('Guess a number from 1-9: '))

if guess1 <= random - 2 :
    print('Guess too small')

elif guess1 + 1 == random :
    print("You're close")

elif guess1 - 1 == random : 
    print("You're close")

elif guess1 >= random + 2 :
    print('Guess too big')

elif guess1 == random :
    print('Congragulations! You Won!')


if guess1 != random :
    guess2 = int(input('Guess a number from 1-9: '))

    if guess2 <= random - 2 :
        print('Guess too small')

    elif guess2 + 1 == random :
        ("You're close")

    elif guess2 - 1 == random :
        print("You're close")

    elif guess2 >= random + 2 :
        print('Guess too big')

    elif guess2 == random :
        print('Congragulations! You Won!')


if guess2 != random :
    guess3 = int(input('Guess a number from 1-9: '))

    if guess3 <= random - 2 :
        print('Guess too small')

    elif guess3 + 1 == random :
        ("You're close")

    elif guess3 - 1 == random :
        print("You're close")

    elif guess3 >= random + 2 :
        print('Guess too big')

    elif guess3 == random :
        print('Congragulations! You Won!')


if guess3 != random :
    guess4 = int(input('Guess a number from 1-9: '))

    if guess4 <= random - 2 :
        print('Guess too small')

    elif guess4 + 1 == random :
        ("You're close")

    elif guess4 - 1 == random :
        print("You're close")

    elif guess4 >= random + 2 :
        print('Guess too big')

    elif guess4 == random :
        print('Congragulations! You Won!')


if guess4 != random :
    guess5 = int(input('Guess a number from 1-9: '))

    if guess5 != random :
        print('You lost. Better luck next time.')

    elif guess5 == random :
        print('Congragulations! You Won!')
