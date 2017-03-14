import random

rng = random.Random()
num = rng.randrange(1, 1000)

guesses = 0
guess = int(input("Guess the number b/w 1 and 1000: "))

while True:
    guesses += 1

    if guess > num:
        print("\n" + str(guess) + " is too high.")
    elif guess < num:
        print("\n" + str(guess) + " is too low.")
    else:
        break

    guess = int(input("Please, try again: "))

print("\nGreat, you got it in {0} guesses!".format(guesses))
