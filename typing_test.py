from timeit import default_timer


print("\n################### Welcome to Typing Test ##################\n")
print("NOTE: There are NO newlines in the typing test. Keep writing!")

para = "The Bat and the Weasels: A Bat who fell upon the ground and was caught by a Weasel pleaded to be spared" \
       " his life. The Weasel refused, saying that he was by nature the enemy of all birds. The Bat assured him" \
       " that he was not a bird, but a mouse, and thus was set free. Shortly afterwards the Bat again fell to the" \
       " ground and was caught by another Weasel, whom he likewise entreated not to eat him. The Weasel said that" \
       " he had a special hostility to mice. The Bat assured him that he was not a mouse, but a bat, and thus a " \
       "second time escaped. It is wise to turn circumstances to good account. "

words = len(para.split())

print("\n################### Press ENTER to start ####################")
print("################# Press ENTER when complete #################\n")
print(">", para)

input()

try:
    start = default_timer()
    inp = input("> ")
    end = default_timer()
    if inp == para:
        total = round(end - start, 2)
        print("\n#############################################################")
        print("\nYou took {} seconds.".format(total))
        total = int(total)/60
        print("Your speed is {} wpm.".format(words//total))

    else:
        print("\n#############################################################")
        print("\nYou mistyped somewhere!")
        print("Please, try again.")

except KeyboardInterrupt:
    print("")


