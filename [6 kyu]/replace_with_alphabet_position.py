# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da/python

# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.


# Sample input:
# "The sunset sets at twelve o' clock."

# Sample output:
# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


import string


def alphabet_position(text):
    indexes = "".join(str(string.ascii_lowercase.index(letter) + 1) + " " for letter in text.lower() if
                      letter in string.ascii_lowercase).strip()
    return indexes


print(alphabet_position("The sunset sets at twelve o' clock."))
