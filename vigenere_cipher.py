"""To implement Vigenere Cipher using:
Given i is the current letters' index in regards to our alphabet and k is the rotation(key):
encryption: c[i] = (p[i] + k[j]) % 26
decryption: p[i] = (c[i] - k[j]) % 26"""

from itertools import cycle

mode = input("Enter 'e' for encrypt or 'd' for decrypt: ")
while mode != 'e' and mode != 'd':
        mode = input("Oops! That was not a valid input. Please try again: ")


def vigenere(text, key):
    """works ONLY for limited size input!"""
    text_output = ""

    for ch, i in zip(text, cycle(key)):
        k = (ord(i.upper()) - 65) % 26
        if ch.isalpha():
            if ch.isupper():
                if mode == 'e':
                    text_output += chr((((ord(ch)) - 65) + k) % 26 + 65)
                elif mode == 'd':
                    text_output += chr((((ord(ch)) - 65) - k) % 26 + 65)
            elif ch.islower():
                if mode == 'e':
                    text_output += chr((((ord(ch)) - 97) + k) % 26 + 97)
                elif mode == 'd':
                    text_output += chr((((ord(ch)) - 97) - k) % 26 + 97)
            k += 1
        else:
            text_output += ch

    return text_output

text = input("Enter the text you want to encrypt/decrypt: ")
key = input("Enter the key: ")
print(vigenere(text, key))

