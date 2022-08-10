# Persistent Bugger.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.


# Sample input:
# 39

# Sample output:
# 3


def persistence(num):
    counter = 0
    while len(str(num)) > 1:
        result = 1
        for digit in str(num):
            result *= int(digit)
        num = result
        counter += 1
    return counter


print(persistence(39))
