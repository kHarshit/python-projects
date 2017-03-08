import random

print("A quiz")
print("===========")

my_dict = {

                "Base-2 number system": "binary",
                "Number system that uses the characters 0-F": "hexadecimal",
                "7-bit text encoding standard": "ascii",
                "16-bit text encoding standard": "unicode",
                "A number that is bigger than the maximum number that can be stored": "overflow",
                "8 bits": "byte",
                "1024 bytes": "kilobyte",
                "Picture Element. The smallest component of a bitmap image": "pixel",
                "A continuously changing wave, such as natural sound": "analogue",
                "A binary representation of a program": "machine code"
}

playing = True
score = 0

while True:
    try:
        n = int(input("How many questions would you like?: "))
        break
    except ValueError:
        print("Oops! That was not a valid no. Please try again.")


while playing:
    for i in range(n):
        question = random.choice(list(my_dict.keys()))  # question is one of the dictionary keys, picked at random
        answer = my_dict[question]  # answer is value of dictionary key
        print("Question " + str(i+1))
        print(question + "?")

        guess = input("> ")

        if guess.lower() == answer.lower():
            print("Correct")
            score += 1
        else:
            print("Nope")

    play_again = input("Enter 'y' to play again, any key to quit: ")

    if play_again.lower() == 'y':
        playing = True
    else:
        playing = False

    print("Your final score is: ", score)
