import random


player_number = int(input("Pick a number between 1 and 100: "))
guess_list = []

while len(guess_list) < 5:
    computer_guess = random.randint(1, 100)
    print("I guess {}.".format(computer_guess))
    if computer_guess > player_number:
        guess_list.append(computer_guess)
        guesses_left = 5 - len(guess_list)
        print("That number is too high. You've taken {} turns.".format(len(guess_list)))
    elif computer_guess < player_number:
        guess_list.append(computer_guess)
        guesses_left = 5 - len(guess_list)
        print("That number is too low. You've taken {} turns".format(len(guess_list)))
    else:
        guess_list.append(computer_guess)
        print("You guessed it in {} turns!".format(len(guess_list)))
        break
else:
    print("You ran out of guesses! The number was {}".format(player_number))