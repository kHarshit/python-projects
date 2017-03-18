# To implement Caesar Cipher using:
# Given i is the current letters' index in regards to our alphabet and k is the rotation(key):
# c[i] = (p[i] + k) % 26  # encryption
# p[i] = (c[i] - k) % 26  # decryption

mode = input("Enter 'e' for encrypt or 'd' for decrypt: ")
while mode != 'e' and mode != 'd':
        mode = input("Oops! That was not a valid input. Please try again: ")


def caesar(text, key):
    text_output = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                if mode == 'e':
                    text_output += chr((((ord(ch)) - 65) + key) % 26 + 65)
                elif mode == 'd':
                    text_output += chr((((ord(ch)) - 65) - key) % 26 + 65)
            elif ch.islower():
                if mode == 'e':
                    text_output += chr((((ord(ch)) - 97) + key) % 26 + 97)
                elif mode == 'd':
                    text_output += chr((((ord(ch)) - 97) - key) % 26 + 97)
        else:
            text_output += ch

    return text_output

text = input("Enter the text you want to encrypt/decrypt: ")
k = int(input("Enter the shift: "))
print(caesar(text, k))


# OR


def encrypt(plain_text, shift):
    cipher_text = ""

    for ch in plain_text:
        if ch.isalpha():
            num = ord(ch) + shift  # ord('A') == 65

            if ch.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            if ch.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            cipher_text += chr(num)
        else:
            cipher_text += ch

    return cipher_text

print(encrypt("Kate2:L", 4))


# To decrypt Caesar Cipher:
# // code //


# To brute force Caesar Cipher:
# // code //
