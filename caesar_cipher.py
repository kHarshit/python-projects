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

