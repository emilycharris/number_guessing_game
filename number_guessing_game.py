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
            print("That's not a number between 1 and 100. Try again.")
        elif guess_number > random_number:
            guess_list.append(guess_number)
            guesses_left = 5 - len(guess_list)
            if abs(guess_number - random_number) <= 5:
                print("That number is too high, but you're close. You've taken {} turns.".format(len(guess_list)))
            else:
                print("That number is too high.  You've taken {} turns.".format(len(guess_list)))
        elif guess_number < random_number:
            guess_list.append(guess_number)
            guesses_left = 5 - len(guess_list)
            if abs(guess_number - random_number) <= 5:
                print("That number is too low, but you're close. You've taken {} turns.".format(len(guess_list)))
            else:
                print("That number is too low.  You've taken {} turns.".format(len(guess_list)))
        else:
            guess_list.append(guess_number)
            print("You guessed it in {} turns!".format(len(guess_list)))
            break

else:
        print("You ran out of guesses! The number was {}".format(random_number))

