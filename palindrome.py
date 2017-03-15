def is_word_palindrome(word):
    """Checks if a word is palindrome."""
    word = word.lower()
    word_rev = word[::-1]  # the reverse property of list indexing works on strings too
    if word == word_rev:
        return True
    else:
        return False


def is_palindrome(s):
    """Checks if a string is a palindrome."""

    def to_chars(s):
        """removes whitespaces from the string"""
        s = s.lower()
        ans = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    # def is_pal(s):
    #     if len(s) <= 1:
    #         return True
    #     else:
    #         return s[0] == s[-1] and is_pal(s[1:-1])
    #
    # return is_pal(to_chars(s))
    return is_word_palindrome(to_chars(s))


inp = input("Enter a word/sentence to check if it is palindrome: ")
print(is_palindrome(inp))
