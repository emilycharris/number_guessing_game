import random

random_number = random.randint(1,100)
guess_list = []

while len(guess_list) < 5:

    try:
        guess_number = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("That's not a number")
    else:
        if not guess_number > 0 or not guess_number < 101:
            print("That's not a number between 1 and 100.  Try again")
        elif guess_number > random_number:
            print("That number is too high.  Try again")
            guess_list.append(guess_number)
        elif guess_number < random_number:
            print("That number is too low.  Try again")
            guess_list.append(guess_number)
        else:
            print("You guessed it!  The number was {}".format(random_number))
            guess_list.append(guess_number)
else:
        print("You ran out of guesses! The number was {}".format(random_number))

