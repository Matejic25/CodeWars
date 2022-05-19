# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


# Sample input:
# "Indivisibilities"

# Sample output:
# 2


def duplicate_count(text):
    values = {}
    for symbol in range(len(text)):
        if text[symbol].lower() not in values:
            values[text[symbol].lower()] = 1
        else:
            values[text[symbol].lower()] += 1
    counter = len([i for i in values if values[i] > 1])
    return counter
