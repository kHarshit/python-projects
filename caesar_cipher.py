def caesar(plain_text, shift):
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

        final_character = chr(num)  # chr(65) == 'A'
        cipher_text += final_character

    return cipher_text

text = input("Enter the text you want to encrypt: ")
key = int(input("Enter the shift: "))
print(caesar(text, key))


# To decrypt Caesar Cipher:
# // code //

# To implement Caesar Cipher using:
# Given x is the current letters index in regards to our alphabet and n is the rotation:
# E(x) = (x + n) % 26  # encryption
# D(x) = (x - n) % 26  # decryption
# // code //


# To brute force Caesar Cipher:
# // code //
