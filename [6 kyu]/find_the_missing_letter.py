# Find the missing letter
# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

# Write a method that takes an array of consecutive (increasing) letters as input
# And returns the missing letter in the array.

# Notes:
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.


# Sample input:
# ['a', 'b', 'c', 'd', 'f']

# Sample output
# 'e'


def find_missing_letter(chars):
    import string
    letters = string.ascii_letters
    for i in range(len(letters)):
        if chars[0] != letters[i]:
            pass
        else:
            for j in range(len(chars)):
                if letters[i+j] != chars[j]:
                    return letters[i+j]
                else:
                    pass
    return None


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
