def is_palindrome(word):
    word = word.lower()
    word_rev = word[::-1]  # the reverse property of list indexing works on strings too
    if word == word_rev:
        return "The word you entered is a palindrome."
    else:
        return "NO, the word you entered is not a palindrome."

word = input("Enter a word or number to check if it's palindrome: ")
print(is_palindrome(word))