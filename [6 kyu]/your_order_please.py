# Your order, please
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/python

# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.

# Note:

# Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.


# Sample input:
# "is2 Thi1s T4est 3a"

# Sample output:
# "Thi1s is2 3a T4est"


def order(sentence):
    return_value = ''
    counter = 1
    list_of_words = sentence.split()
    for i in range(len(list_of_words)):
        for word in list_of_words:
            for char in word:
                if char == str(counter):
                    counter += 1
                    return_value += word + " "
                    list_of_words.remove(word)
    return return_value.strip()


print(order("is2 Thi1s T4est 3a"))
