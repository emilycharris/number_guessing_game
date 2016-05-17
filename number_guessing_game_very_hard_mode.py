import random

player_number = int(input("Pick a number between 1 and 100: "))
guess_list = []

minimum = 1
maximum = 100


while len(guess_list) < 5:
    computer_guess = random.randint(minimum, maximum)
    print("I guess {}.".format(computer_guess))
    if computer_guess > player_number:
        guess_list.append(computer_guess)
        guesses_left = 5 - len(guess_list)
        if abs(player_number - computer_guess) <= 5:
            print("That number is too high, but you're close. You've taken {} turns.".format(len(guess_list)))
            maximum = computer_guess - 1
            minimum = computer_guess - 5
        else:
            print("That number is too high.  You've taken {} turns.".format(len(guess_list)))
            maximum = computer_guess - 1
    elif computer_guess < player_number:
        guess_list.append(computer_guess)
        guesses_left = 5 - len(guess_list)
        if abs(player_number - computer_guess) <= 5:
            print("That number is too low, but you're close. You've taken {} turns.".format(len(guess_list)))
            minimum = computer_guess + 1
            maximum = computer_guess + 5
        else:
            print("That number is too low.  You've taken {} turns.".format(len(guess_list)))
            minimum = computer_guess + 1
    else:
        guess_list.append(computer_guess)
        print("You guessed it in {} turns!".format(len(guess_list)))
        break
else:
    print("You ran out of guesses! The number was {}".format(player_number))