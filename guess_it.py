import random

def game():
    # generate a random number 1 - 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(raw_input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number silly".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess >= secret_num:
                print("Lower...")
            elif guess <= secret_num:
                print("Higher...")
            else:
                print("That's not it!")
                guess = ""
            guesses.append(guess)
    else:
        print("You didn't get it! my number was {}.".format(secret_num))

    try:
        play_again = raw_input("Do you want to play again? (Y/n): ")
    except ValueError:
        play_again = "Y"
    else:
        if play_again.lower() != "n":
            game()
        else:
            print("Good Day Good Sir|Miss!")
game()
